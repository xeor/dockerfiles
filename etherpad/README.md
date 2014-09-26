* NOT DONE! *

# info
* Centos6 as base
* runs etherpad-lite
* output goes to port 80
* run with: docker run -i -t --link some-postgres:postgresql -e "TITLE=web title" -e "ADMIN_PW?=apassword" xeor/etherpad bash

# todo
* Run "/etherpad-lite/bin/installDeps.sh" or something at buildtime to fix initial
* External db, set settings(dbType) to "postgres"
* Settings (title, port, defaultPadText, abiword, trustProxy, 
* Non-root user
* abiword
* checkout plugins and hooks
* default admin user, so we can access /admin
