#!/usr/bin/env python

__author__ = 'Lars Solberg'

'''
The sole purpose of this file is to enable google authenticated in the gitlab.yml file.
The settings for doing this is commented out in the upstream gitlab docker repo, so we need to hack this in.
This script might be usefull for other similar stuff as well.
'''

import re
import os
import sys

if not os.environ.get('GITLAB_GOOGLE_AUTH_ENABLED', None):
    sys.exit(0)

under_omniauth = False
min_indention = 100 # Just a temporary high number untill its sat
index = 0

with open('/app/setup/config/gitlabhq/gitlab.yml', 'r') as fp:
    lines = fp.readlines()
    for l in lines:
        try:
            indention = re.search('\S', l).start()
        except AttributeError:
            indention = 0
        key_name = re.match(r' *([^ :]*).*', l).groups()[0]
        if key_name == 'omniauth':
            # Good, we can start looking for our settings now..
            under_omniauth = True
            min_indention = indention + 2 # We dont want to go under this indention again

        if under_omniauth:
            if indention > min_indention:
                break # We are outside omniauth and done looking
            if key_name == 'enabled':
                lines[index] = l.replace('false', 'true')
            if key_name == 'providers':
                lines[index+1] = "%s- { name: 'google_oauth2', app_id: '%s', app_secret: '%s', args: { access_type: 'offline', approval_prompt: '' }}\n" % (
                    ' ' * (indention + 2), os.environ.get('GITLAB_GOOGLE_AUTH_APP_ID', ''), os.environ.get('GITLAB_GOOGLE_AUTH_APP_SECRET', '')
                    )

        index += 1

with open('/app/setup/config/gitlabhq/gitlab.yml', 'w') as fp:
    fp.write(''.join(lines))
