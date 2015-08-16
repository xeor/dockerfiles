#!/usr/bin/env python

import os
import json
import subprocess
from docker import Client

runner_dir = '/runners'
inspect_dir = '/inspects'

c = Client(base_url='unix://var/run/docker.sock')

try:
    os.mkdir(inspect_dir)
except OSError:
    pass


def handler(docker_id, status):
    inspect = c.inspect_container(docker_id)
    valid_events = [e for e in inspect['Config']['Env'] if e.startswith('ACT_')]
    if valid_events.count == 0:
        return
    for e in valid_events:
        key, value = e.replace('ACT_', '').split('=')
        runner_file = '{}/{}'.format(runner_dir, key)
        if os.path.isfile(runner_file):
            inspect_file = '{}/{}.json'.format(inspect_dir, docker_id)
            if not os.path.isfile(inspect_file):
                with open(inspect_file, 'w') as fp:
                    fp.write(json.dumps(inspect, indent=2))
            try:
                subprocess.call([runner_file, value, docker_id, status])
            except OSError:
                # Probably not executable..
                return

for i in c.containers(filters={'status': 'running'}):
    handler(docker_id=i['Id'], status='running')

# c.events() returns a blocking generator
for event in c.events(decode=True):
    handler(docker_id=event['id'], status=event['status'])
