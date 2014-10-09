Splunk in a can, which uses the free 500mb/day version of Splunk as default.
Splunk is an awesome log-analyzer, check out more information at http://www.splunk.com/

* Splunk wont always run depending on the underlying filesystem. I noticed this while using boot2docker, so it might not work there..
* This container is ment for testing Splunk, or running it with free version home, not on internet.
  * Configurations is not best practise
  * Security might not be optimal
  * Splunk have said nothing about running in Docker
  * Have no idea how fast/slow it will run..
  * And so on... Use it for test :)

# Run

Start the container with something like `docker run -d -P xeor/splunk` (to test it out). For using it for something useful, use volumes and see `Use-cases` below..

* It will automaticly start to listen on 514 tcp/udp and set sourcetype to `syslog`

## Use-cases

* Quickly spin up a "throw-away" Splunk to view your local /var/log/. ^c when done..
  * docker run -i -t -v /var/log/:/data/ -p 8000:8000 --rm xeor/splunk

* Develop/labbing on an app with inputs from a folder
  * docker run -i -t -v $PWD/logfolder/:/testdata/ -v $PWD/testapp:/opt/splunk/etc/apps/testapp -p 8000:8000 --rm xeor/splunk
  * Point the inputs files in your testapp to /testdata and see how splunk indexes it.
  * Have Splunk/Docker in one terminal, and develop in another. When you want to reindex, just hit ^c in Docker <UP><ENTER> and you are good to go again with a new fresh index.

* Test misc Splunk configurations
  * docker run -i -t -p 8000:8000 --rm xeor/splunk bash
  * Edit `/opt/splunk` files as you normally would
  * Start and restart with normal `/opt/splunk/bin/splunk start` `/opt/splunk/bin/splunk restart` and so on. No magic.
  * When you are done, just exit the shell, the container will be gone.

* Figure out when your files have been changed (this is obiously just an example of all the fun you can do)..
  * docker run -i -t -p 8000:8000 -p 514:514 --rm xeor/splunk
  * find /etc -print0 | xargs -0 stat -c "%z %n" | nc localhost 514
  * Do a search for `sourcetype=syslog | fields _time, filename` and get a visual representation of when the files have changed..

## Volumes
* `/opt/splunk/var/lib/splunk`: For the splunk data
* `/data`: If it exists/is-mounted, we will add it and monitor it (great for a quick test).
* `/license.lic`: Splunk license to add.. Not 100% sure if this is working or not.. Give me a heads up if it does/doesn't :)

## Environment variables available
* `SPLUNK_SERVERNAME`: If sat, it will become the name of the Splunk instance, and the name of the host for the default input.
* `SPLUNK_ENTERPRISE`: Set to `true` if you want the enterprise 30days trial (default is the free 500MiB/day license). Should become normal enterprise if /license.lic is mounted (see volumes)
* `SPLUNK_PW`: Set to the password you want to use if you are using the enterprise trial. Default to `changeme`
* `SPLUNK_WEB_PATH`: Set the relative path for Splunks web-endpoint. (Example `splunk`) for having Splunk under http://domain/splunk. Useful behind reverse proxies..
* `SPLUNK_SESSION_TIMEOUT`: Timeout for the web-service. Use number and one of smhd, example `7d` for 7 days
* `SPLUNK_SSO`: Must be sat to `true` to enable the SSO options
* `SPLUNK_SSO_ALLOW_FROM`: Either set an ip here for the proxy the request is coming from. Or if its a Docker container, you can link it as `proxy` like `--link nginx_reverse:proxy`, and we will detect it.
* `SPLUNK_SSO_REMOTEUSER`: If you want Splunk to be able to do autologin via http-header from eg an intermidiate proxy. Set to eg `USER`. To debug (`http://splunk/debug/sso`). Should enable an extra admin-user as well with the username of the `USER` env. This setting also enables the SSO option in Splunk.
* `SPLUNK_SSO_ADMIN`: username for an extra admin-user that we will add (with password "password"), only use this to get SSO with `SPLUNK_WEB_REMOTEUSER` to work. Its ment for SSO.

# Config
* The folder named `main_app` is basicly an empty app. You can use it (or a new app) as volumes mounted to something like `/opt/splunk/etc/apps/main`.
  * Use this method to "install" new apps as well if you want them persistent.
