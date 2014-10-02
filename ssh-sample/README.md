# Controll
* Build it: docker build -t tagname .
* Run: docker docker run -d -P tagname
* Access monit console: Access port mapped to 2812
* Ssh: ssh into port mapped to 22 using the username "admin" and the key you put in "authorized_keys"

# Info
* centos base image with EPEL
* ssh enabled with key, own user and sudo
* monit enabled
* Entrypoint script enabled
* Use it as a template for creating private services in Docker
