* Container that talks to SickBeard, asks for shows that belongs to network in (NRK1, NRK2, NRK3) and have status `Wanted`, and downloads them to the folder you have them stored on, in SickBeard.
* Mount the volume SickBeard expects to store the folder in at the same place in this container! IE, if SickBeard uses folder /Series/..., mount it as /Series in this container as well.
* The `worker.py` file contains many more NRK-rip godies. Feel free to use them. I've tried to keep the component somewhat separate, so they are easy to use on each own.. (Like keeping the search logic from download_by_episode_url).
* The name pattern in SickBeard that this works with out of the box is `S%0S/S%0SE%0E - %EN` (S02/S02E03 - Ep Name.ext)
* Be nice to NRK, dont just download everything! This container was created for fun, and to create a template for similar containers only, not for general usage. Use at your own risk..

# env
* `SCAN_TIME`: How often we will check if we can find any wanted episodes (in seconds!). Default 86400
* `SICKBEARD_URL`: Sickbeard url. With schema, and without trailing /
* `SICKBEARD_API_KEY`: Api key. Remember to enable this in Sickbeard settings

# todo
* entrypoint script to download manually.
* cron-like timer
* smarter timer, we know when the show runs
* support for other sites, like nrksuper
* support for weird episodenames, some of the shows got date-names
