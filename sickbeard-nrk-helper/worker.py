import os
import re
import json
import logging
import itertools
import subprocess

from bs4 import BeautifulSoup
import requests

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())  # Defaulting to null output in case Caculator class is imported


class Ripper:

    search_url = 'http://tv.nrk.no/sokmaxresults?q={query}&page=0'
    season_list_url = 'http://tv.nrk.no/program/Episodes/{show_name_slug}/{season_id}/{program_id}'
    show_url = 'http://tv.nrk.no{show_uri}'

    def __init__(self, query):
        self.query = query

    def find_show_url(self, query):
        data = requests.get(self.search_url.format(query=query))
        soup = BeautifulSoup(data.content)
        show_url = None
        for i in soup.findAll('h3', {'class': 'listobject-title'}):
            if i.text.strip().lower() == query.lower():
                show_url = i.parent.parent.find('a', {'class': 'listobject-link'}).get('href')
                break

        logger.debug('Found show-url: {}'.format(show_url))
        return show_url

    def get_season_urls(self, show_url):
        seasons = []
        data = requests.get(show_url)
        soup = BeautifulSoup(data.content)
        show_name_slug = re.search(r'[^/]+$', show_url).group(0)
        program_id = soup.find('meta', {'name': 'programid'}).get('content')

        for i in soup.findAll('a', {'class': 'season-link'}):
            season_id = i.get('data-season')
            if season_id is None:
                continue
            number = re.search(r'[0-9]', i.get('title')).group(0)
            season_url = self.season_list_url.format(
                show_name_slug=show_name_slug, season_id=season_id, program_id=program_id
            )
            number = number.zfill(2)
            seasons.append({'url': season_url, 'number': number})
            logger.debug('Found season_id {} (S{}), adding url {}'.format(season_id, number, season_url))
        return seasons

    def _get_short_name(self, text):
        # Generate short-names like "S02E12" from how the URL/URI looks like
        numbers = re.findall(r'sesong-([0-9]+)/episode-([0-9]+)', text)[0]
        return {
            'shortname': 'S{}E{}'.format(numbers[0].zfill(2), numbers[1].zfill(2)),
            'season': numbers[0].zfill(2),
            'episode': numbers[1].zfill(2)
            }

    def get_shows_in_season_url(self, season_url):
        logger.debug('Getting shows from season-url: {}'.format(season_url))
        shows = []
        data = requests.get(season_url)
        soup = BeautifulSoup(data.content)

        for show in soup.findAll('li', {'class': 'episode-item'}):
            uri = show.find('a').get('href')
            names = self._get_short_name(uri)
            entry = {
                'url': self.show_url.format(show_uri=uri),
                'episode_id': show.get('data-episode'),
                'shortname': names['shortname'],
                'episode_number': names['episode'],
                'season_number': names['season']
            }
            shows.append(entry)
            logger.debug('Adding episode_id {episode_id} (S{shortname}) with url {url}'.format(**entry))

        return shows

    def get_shows_by_url(self, show_url):
        shows = []
        for season in self.get_season_urls(show_url):
            for show in self.get_shows_in_season_url(season['url']):
                shows.append(show)

        return shows

    def download_show(self, show_url, folder):
        logger.debug('Downloading show via url: {}'.format(show_url))
        data = requests.get(show_url)
        soup = BeautifulSoup(data.content)
        names = self._get_short_name(show_url)

        master_playlist = soup.find('div', {'id': 'playerelement'}).get('data-hls-media')

        # This playlist contains several resolutions. We want the highest
        data = requests.get(master_playlist)
        show_playlist = sorted(re.findall(r'.*index_[0-9]+_av.*', data.text))[-1]
        logger.debug('Starting download of {} from playlist {}'.format(names['shortname'], show_playlist))
        try:
            os.makedirs('{}/{}'.format(folder, names['season']))
        except FileExistsError:
            pass
        subprocess.call([
            '/usr/bin/ffmpeg',
            '-i', show_playlist,  # Input
            '-vcodec', 'copy',    # Use the same videocodec
            '-acodec', 'copy',    # As for audio
            '-hide_banner',       # Nothing we need
            '/{}/S{}/{}.mkv'.format(folder, names['season'], names['shortname'])
        ])

    def filter_out_existing(self, wanted_shows, path):
        """
        Filenames we check against might be in any subfolder, like path/S02/...
        As long as their name contains like *S02E12* in the name, we will find it.
        """
        shows = []

        # Get 1 list of all the files beneth path, recursive
        existing_files = list(itertools.chain(*[i[2] for i in os.walk(path)]))

        for show in wanted_shows:
            shortname = show['shortname']
            logger.debug('Checking if show {} exists in {}'.format(shortname, path))
            exist = False if len([x for x in existing_files if shortname.lower() in x.lower()]) == 0 else True
            if exist:
                logger.debug('  Found it, wont re-download')
            else:
                logger.debug('  Did not exist, adding it to download queue')
                shows.append(show)

        return shows

    def download_missing_in_folder(self, folder):
        show_url = self.find_show_url(self.query)
        if not show_url:
            return None

        shows = self.get_shows_by_url(show_url)
        shows = self.filter_out_existing(shows, folder)
        for show in shows:
            self.download_show(show['url'], folder)

    def download_episodes(self, wanted_shows, folder):
        shows = []  # The ones we will download
        show_url = self.find_show_url(self.query)
        if not show_url:
            return None
        for show in self.get_shows_by_url(show_url):
            if show['shortname'] in wanted_shows:
                self.download_show(show['url'], folder)


class SickBeard:

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        self.base_url = '{}/api/{}'.format(url, api_key)
        logger.debug('Setting base url for SickBeard to {}'.format(self.base_url))

    def get_show_with_networks(self, networks):
        # Networks is a list, so we can support networks with multiple names, like "NRK".
        # Its totally fine to only have 1 entry in the list
        shows = []
        data = requests.get('{}/?cmd=shows'.format(self.base_url))
        data = json.loads(data.text)
        show_ids = [i for i in data['data'] if data['data'][i]['network'] in networks]
        logger.debug('Found {} as shows matching one of the network ({})'.format(show_ids, networks))
        for show_id in show_ids:
            data = requests.get('{}/?cmd=show&tvdbid={}'.format(self.base_url, show_id))
            data = json.loads(data.text)
            shows.append({
                'sb_id': show_id,
                'path': data['data']['location'],
                'name': data['data']['show_name']
            })
        return shows

    def get_wanted_in_network(self, network):
        shows = {}
        for show in sb.get_show_with_networks(['NRK1', 'NRK2', 'NRK3']):
            shows[show['sb_id']] = {'path': show['path'], 'name': show['name'], 'missing': []}
            data = requests.get('{}/?cmd=show.seasons&tvdbid={}'.format(self.base_url, show['sb_id']))
            data = json.loads(data.text)
            for season in data['data']:
                for episode in data['data'][season]:
                    if data['data'][season][episode]['status'] == 'Wanted':
                        shortname = 'S{}E{}'.format(season.zfill(2), episode.zfill(2))
                        shows[show['sb_id']]['missing'].append(shortname)

        logger.debug('The episodes we want is: {}'.format(shows))
        return shows

    def refresh(self, show_id):
        # FIXME: Rename episodes...? Not an API?
        logger.debug('Refreshing/updating show {} in SickBeard'.format(show_id))
        requests.get('{}/?cmd=show.refresh&tvdbid={}'.format(self.base_url, show_id))
        requests.get('{}/?cmd=show.update&tvdbid={}'.format(self.base_url, show_id))

if __name__ == '__main__':
    logger.addHandler(logging.StreamHandler())  # Display info when running script manually
    logger.setLevel(logging.DEBUG)  # Set to logging.DEBUG for debug

    sb = SickBeard(os.environ.get('SICKBEARD_URL'), os.environ.get('SICKBEARD_API_KEY'))
    for show_id, data in sb.get_wanted_in_network(['NRK1', 'NRK2', 'NRK3']).items():
        Ripper(data['name']).download_episodes(data['missing'], data['path'])
        sb.refresh(show_id)
