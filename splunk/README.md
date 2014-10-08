# NOT DONE!! #

Splunk in a can, which uses the free 500mb/day version of Splunk.
Splunk is an awesome log-analyzer, check out more information at http://www.splunk.com/

# Checkout
* system/default/web.conf: "remoteUser = REMOTE_USER", "SSOMode = strict", "# tools.proxy.on = True" 
* system/default/server.conf: "serverName=$HOSTNAME"
* system/local/inputs.conf: "host = fe949a5ffe17"
* system/local/server.conf: "serverName = fe949a5ffe17", 

# Build
Since we cant download the splunk rpm in the building process. You need to build this container yourself.

1. Download the Dockerfile
2. Download the splunk rpm
3. Name it splunk.rpm and put it in the same folder as the Dockerfile
4. Run `docker build -t splunk .`

# Run

Start the container with something like `docker run -d -P xeor/splunk` (to test it out). For using it for something useful, use volumes..

* It will automaticly start to listen on 514/udp and set sourcetype to `syslog`

## Volumes
* `/opt/splunk/var/lib/splunk`: For the splunk data
* `/data`: If it exists/is-mounted, we will add it and monitor it (great for a quick test).

## Environment variables available
* `SPLUNK_PW`: FIXME
* `SPLUNK_WEB_PATH`: FIXME (root_endpoint in "system/default/web.conf")

# Config
* The folder named `main_app` is basicly an empty app. You can use it (or a new app) as volumes mounted to something like `/opt/splunk/etc/apps/main`.
  * Use this method to "install" new apps as well if you want them persistent.
