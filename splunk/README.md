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

Start the container with something like:

    docker run -d -p 80:80 -v /path/to/datastore:/data -v /path/to/configs:/conf xeor/splunk

## Environment variables available
* `LOGLEVEL`: Set to `debug` to see output from supervisord and Splunks stdout.
* `SPLUNK_PW`: FIXME
* `SPLUNK_WEB_PATH`: FIXME (root_endpoint in "system/default/web.conf")

# Config - FIXME
* Splunk will automaticly restart (via inotify) if you change any files in the configuration directory
