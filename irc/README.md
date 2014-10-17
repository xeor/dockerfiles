This container contains (get it..), what I find as a `pretty good` irc setup.
It might not be what you like, and not even the best. But its what I found without trying every irc client/setup there is...

# info
* CentOS 7

# usage
* WeeChat is compiled with perl, tcl, lua, ruby and python plugins. But no scripts are enabled as default.
  * Install/enable plugins inside WeeChat (using `/script`)
    * Look at http://weechat.org/scripts/ for info

# todo
* Find a better name? Mix of weechat/bitlebee might end up beeing much more than `irc`..

## tmux
* auto start

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

# environment variables
* None? Just autogenerate configuration and make it custimizable..? Logic of what stuff is called instead 
