# NOT DONE!! #

Splunk in a can, which uses the free 500mb/day version of Splunk.
Splunk is an awesome log-analyzer, check out more information at http://www.splunk.com/

# Checkout
* License? How to check?
* system/default/web.conf: "remoteUser = REMOTE_USER", "SSOMode = strict" 
* system/default/server.conf: "serverName=$HOSTNAME"
* system/local/inputs.conf: "host = fe949a5ffe17"
* system/local/server.conf: "serverName = fe949a5ffe17", 

# Run

Start the container with something like `docker run -d -P xeor/splunk` (to test it out). For using it for something useful, use volumes and see `Use-cases` below..

* It will automaticly start to listen on 514/udp and set sourcetype to `syslog`

## Use-cases

* Quickly spin up a "throw-away" Splunk to view your local /var/log/. ^c when done..
  * docker run -i -t -v /var/log/:/data/ -p 8000:8000 --rm xeor/splunk

* Develop/labbing on an app with inputs from a folder
  * docker run -i -t -v $PWD/logfolder/:/testdata/ -v $PWD/testapp:/opt/splunk/etc/apps/testapp -p 8000:8000 --rm xeor/splunk
  * Point the inputs files in your testapp to /testdata and see how splunk indexes it.
  * Have Splunk/Docker in one terminal, and develop in another. When you want to reindex, just hit ^c in Docker <UP><ENTER> and you are good to go again with a new fresh index.

## Volumes
* `/opt/splunk/var/lib/splunk`: For the splunk data
* `/data`: If it exists/is-mounted, we will add it and monitor it (great for a quick test).

## Environment variables available
* `SPLUNK_ENTERPRISE_TRIAL`: Set to `true` if you want the enterprise 30days trial (default is the free 500MiB/day license)
* `SPLUNK_PW`: Set to the password you want to use if you are using the enterprise trial. Default to `changeme`
* `SPLUNK_WEB_PATH`: Set the relative path for Splunks web-endpoint. (Example `splunk`) for having Splunk under http://domain/splunk
* `SPLUNK_BEHIND_PROXY`: Set to `true` if you are using Splunk behind a reverse proxy.

# Config
* The folder named `main_app` is basicly an empty app. You can use it (or a new app) as volumes mounted to something like `/opt/splunk/etc/apps/main`.
  * Use this method to "install" new apps as well if you want them persistent.
