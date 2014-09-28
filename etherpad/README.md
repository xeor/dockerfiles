# info
* Centos6 as base
* runs etherpad-lite
* Asumes some settings.. Take a look at settings.json, and fork this repo if you want something else. Its really just made quick and dirty for a local project :)
* run: docker run -d --link postgres:postgresql -e "TITLE=web title" -e "ADMIN_PW=pass" -e "DEFAULT_PAD_TEXT=start writing" -p 80:8080 xeor/etherpad
