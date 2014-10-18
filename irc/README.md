** NOT READY, dont use! **

This container contains (get it..), what I find as a `pretty good` irc setup.
It might not be what you like, and not even the best. But its what I found without trying every irc client/setup there is...

# info
* CentOS 7
* Runs as non-priv (`irc`) user
* Every service built from source (not sshd and tmux), so you can customize/compile in/get the newest/hottest...
* A mix of tmux, sshd, WeeChat, BitleBee, Wetty and Glowing Bear
  * tmux: WeeChat runs in here, used to get a detachable run with possibility for multiple open attached clients
  * sshd: So you can login via your key via ssh.
  * WeeChat: The "chat" client (irssi but better), which is much more than just a chat client..
  * BitleBee: Works as a gateway for non-irc channels, like Gtalk, Twitter and so on..
  * Wetty: A web-terminal that works perfectly (but only in Chrome). You can access the tmux session with WeeChat via this.
  * Glowing Bear: An html5 client that connects directly to WeeChat. It looks very good and even support html5 notifications.

# usage
* Recommended setup is to use `fig` and the `fig.yml` file that follows. Just make a copy of it and put it in its own folder with all your data directories..
* Run container with something like `docker run -e "VAR1=something" -v ${PWD}/data:/data --rm xeor/irc`.
  * Make sure you read the environment varaiables you can set when running the container.
  * The data mount will get populated the way it should be if its empty.
    * There is also a self-signed certificat that is generated under `weechat/ssl/relay.pem`. It is used for Glowing Bear connection. You should replace this cert with a real one...
* WeeChat is compiled with perl, tcl, lua, ruby and python plugins. But no scripts are enabled as default.
  * Install/enable plugins inside WeeChat (using `/script`)
    * Look at http://weechat.org/scripts/ for info
* Both Wetty and Glowing Bear will be patched so that they autologin and connects to the right server (your WeeChat). Read about security below.
  * Wetty runs `/usr/bin/su irc -c /bin/bash -l`, instead of `/bin/login`. The `irc` user bashrc attaches to the tmux session at login, so you will end up right inside your WeeChat.
  * Glowing Bear is tricky, but here, we are patching its index.html to set the html5 storage data to the correct values before it starts, including autologin=true..
* To `ssh` into your setup, use the `irc` as a user, and the key you defined when you started your container.

# security
* Both Wetty and Glowing Bear will autologin, so dont run this setup as it is!
* The recommended way is to use the setup described in the fig.yml file. You can use `fig up -d` to start up everything.
  * Basicly, run this setup behind an reverse http proxy with authentication.

# environment variables
* `SSH_KEY`: The public key you want to use to login via ssh.

# todo
* Find a better name? Mix of weechat/bitlebee might end up beeing much more than `irc`..
* Put all services in supervisord

## WeeChat
* Info about common configurations
* Info about setting relay password to `{{auto_gb_pw}}` if it should be generated at container start, and pre-filled into glowing bear
* Example config http://pascalpoitras.com/my-weechat-configuration/

## Glowing Bear

### Glowing Bear - autoconnect
* Make a switch to add autoconnection when you visit the glowing bear site. This is an html5 app, so we need to do some tricks.
  Plan is to add local storage elements when page is visited, then redirect to the "real" glowing bear page..

  * <script>localStorage.setItem("name", "value"); ....</script>
  * redirect
  * <script>localStorage.removeItem("name"); ...</script> // or hook into connection.js and after $log.info("Connected to relay"); to remove entries..

#### List of offline/local-storage entries we need to add
autoconnect     true
fontfamily      "Inconso..."    // We can delete this. It will be created
fontsize        "14px"          // same for this
host            "localhost"     // From environment-variable
hotlistsync	true
noembed         true
nonicklist      false
onlyUnread      false
orderbyserver   true
password        ""              // Auto generated and match
port            "9001"          // Default 9001, but configurable
proto           "weechat"
readlineBindings false
savepassword    true
showtimestamp   true
showtimestampSeconds true
soundnotification    false      // Environment variable?
ssl             false           // true
useFavico       true


## bitlebee (http://www.bitlbee.org/)
* Config files
* libpurple (to support more protocols) http://wiki.bitlbee.org/

# environment variables
* None? Just autogenerate configuration and make it custimizable..? Logic of what stuff is called instead 
