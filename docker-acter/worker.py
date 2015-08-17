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
    procs = []
    inspect = c.inspect_container(docker_id)
    valid_events = [e for e in inspect['Config']['Env'] if e.startswith('ACT_')]
    if valid_events.count == 0:
        return
    for e in valid_events:
        key, value = e.replace('ACT_', '').split('=')
        runner_file = '{}/{}'.format(runner_dir, key)
        if os.path.isfile(runner_file):
            inspect_file = '{}/{}_{}.json'.format(inspect_dir, docker_id, status)
            with open(inspect_file, 'w') as fp:
                fp.write(json.dumps(inspect, indent=2))
            try:
                # We need to keep a referrence to the process so we can remove the reference
                # when they are done. See comment below.
                # We also need to spawn the process in the backround, therefor, Popen, not call.
                procs.append(subprocess.Popen([runner_file, value, docker_id, status]))

                # Delete the references to completed processes so python will do garbage collection
                # to kill old processes. They will be zombies from the time they are done to when
                # this code is run. A zombie doesnt use any resources, but its nice to get rid of them.
                procs[:] = [proc for proc in procs if proc.poll() is None]
            except OSError:
                # Probably not executable..
                return

for i in c.containers(filters={'status': 'running'}):
    handler(docker_id=i['Id'], status='running')

# c.events() returns a blocking generator
for event in c.events(decode=True):
    handler(docker_id=event['id'], status=event['status'])
