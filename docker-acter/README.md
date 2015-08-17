This container runs code based on Docker containers environment-variables it sees.

The environment variable must start with `ACT_`, example `ACT_FOO`.
Example, if you want to do something when `ACT_FOO` is detected (run a container with `-e "ACT_FOO=bar"`), make a script and map it under `/runners/FOO`, and you are done. This container will now run `/runners/FOO bar 5795ee560ff5c4f85d57820c4ac7474963c3f0f882f372db6ef515832dee22fb create` ("create" is the eventtype and all of the events docker suports is sent to the runner, one by one). The information from docker inspect CONTAINER_ID is saved as a json file in `/inspects/5795ee560ff5c4f85d57820c4ac7474963c3f0f882f372db6ef515832dee22fb_create.json` where your script can grab it.
This json file will be overwritten every time we have a valid ACT_ environment-variable, is detected, and for that specific event. That might not happend so much tho :)
Some information is not available in all state jsons; like IPAddress..

We will also do an initial check on all running containers, and in those cases, we will use the status `running`

If there are multiple variables sat, several runners will be runned..

It is up to you what happens next :)

Remember that your runners needs to be executable (+x), and the docker socket (`-v /var/run/docker.sock:/var/run/docker.sock`) needs to be mounted.

# Included runners

## NETACCESS - Controll access subnets (usually, your local lan)
* The idea is to default deny containers access to your local network, but still let them go online.
* A way for overriding this, so you can start containers with eg. `-e "ACT_NETACCESS=10.0.0.0/8"`, if you want them access to your LAN.

Make a firewall rule for what you want to block as default. Something like `iptables -I FORWARD -d 10.0.2.0/24 -j DROP`

The container needs a little more access than usual; `docker run -d -v /var/run/docker.sock:/var/run/docker.sock --cap-add NET_ADMIN --net=host xeor/docker-acter` should do the trick.

NETACCESS prepends iptables forward ACCEPT rules to the FORWARD chain, so your containers can now go places based on your environment-variables.
You can also specify several `-e ACT_NETACCESS` if you want. They will all be added.
The rules will be removed on the Docker event `die` and added on 'create'
