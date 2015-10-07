This container runs code based on Docker containers environment-variables it sees.

The environment variable must start with `ACT_`, example `ACT_FOO`.
Example, if you want to do something when `ACT_FOO` is detected (run a container with `-e "ACT_FOO=bar"`), make a script and map it under `/runners/FOO`, and you are done. This container will now run `/runners/FOO bar 5795ee560ff5c4f85d57820c4ac7474963c3f0f882f372db6ef515832dee22fb create` ("create" is the eventtype and all of the events docker suports is sent to the runner, one by one). The information from docker inspect CONTAINER_ID is saved as a json file in `/inspects/5795ee560ff5c4f85d57820c4ac7474963c3f0f882f372db6ef515832dee22fb_create.json` where your script can grab it.
This json file will be overwritten every time we have a valid ACT_ environment-variable, is detected, and for that specific event. That might not happend so much tho :)
Some information is not available in all state jsons; like IPAddress..

We will also do an initial check on all running containers, and in those cases, we will use the status `running`

If there are multiple variables sat, several runners will be runned..

It is up to you what happens next :)

Remember that your runners needs to be executable (+x), and the docker socket (`-v /var/run/docker.sock:/var/run/docker.sock`) needs to be mounted.

Check out https://docs.docker.com/reference/api/docker_remote_api/ for a good list of events that docker triggers that you can use in the runners.

# Included runners

## NETACCESS - Controll access subnets (usually, your local lan)
* The idea is to default deny containers access to your local network, but still let them go online.
* A way for overriding this, so you can start containers with eg. `-e "ACT_NETACCESS=10.0.0.0/8"`, if you want them access to your LAN.

Make a firewall rule for what you want to block as default. Something like `iptables -I FORWARD -d 10.0.2.0/24 -j DROP`

This runner needs special network access; `docker run -d -v /var/run/docker.sock:/var/run/docker.sock --cap-add NET_ADMIN --net=host xeor/docker-acter` should do the trick.

NETACCESS prepends iptables forward ACCEPT rules to the FORWARD chain, so your containers can now go places based on your environment-variables.
You can also specify several `-e ACT_NETACCESS` if you want. They will all be added.
The rules will be removed on the Docker event `die` and added on 'create'

We are not setting any ESTABLISHED,RELATED rules. So if you example want a client (10.1.2.3) to be able to access your container, you will need to add that to ACT_NETACCESS as well..

## WEBFEWD
`webfewd` stands for Web Forward a set Environmen-variable from Wildcard DNS.. Or something... :)

It can be used togheter with a wildcard nginx redirection to spin up web-domains based on an environment variable you are setting on your Docker container.

Example;
* Start this container with something like; `docker run -d -v /var/run/docker.sock:/var/run/docker.sock -p 8008:80 --net=host ...`
* Given the dns record `*.dev-domain`, being redirected to `1.2.3.4`, you can have nginx on `1.2.3.4:80` redirecting traffic that goes to `*.dev-domain` to `localhost:8008`.
* If you start a container now with `-e ACT_WEBFEWD=test1.dev-domain`, this container will now detect the container, and generate nginx config that sends `test1.dev-domain` to the container with the environment-variable `ACT_WEBFEWD=test1.dev-domain` and whatever port that it uses to listen on for web (port 80 or 8080!).

We need docker.sock mounting to see docker events. And we need to be on `--net=host` so we can forward to localhost.

## NAT - Tell a router that it should forward packages to us (not done!)
* First of all, this runner is not done. Its mostly done, and you can look at how it works. It kinda works for mikrotik but its not 100%
* The idea is to use add nat rules in your gateway when the container starts so it can start receiving traffic.
* A container started with example `-e ACT_NAT=80` will contact the gateway and make sure the dockerd host machine gets port 80.
* You can also start it with `-e ACT_NAT=80:8000` if you want the router ip of port 80 to be routed to this dockerd host port 8000.
* We wont do anything unless this container exposes the port you want.

This runner needs special network access; `docker run -d -v /var/run/docker.sock:/var/run/docker.sock --net=host xeor/docker-acter` should do the trick. This is to get the IP we need to make the opening to. Alternativ, you can run this container with `-e PUBIP=1.2.3.4`.

It works with contacting, checking and creating NAT rules on your gateway using the port specified as inbound port.
If the port is already defined, we wont override the rule unless you also start the container with `-e NAT_FORCE=true` (true being any value).

You must define a `NAT_VENDOR` as well, currently supported is only `mikrotik`.

* `mikrotik` nat-vendor needs;
  * `MIKROTIK_LOGIN`, if other than `admin@10.0.0.1`
  * The ssh key that got access to firewall mounted in as `/mikrotik_ssh.key`.
  * `MIKROTIK_ININTERFACE` if other than `ether1-gateway`
  *
