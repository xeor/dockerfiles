* Lynis is a free and opensource auditing tool from Cisofy (with an enterprise brother), located at http://cisofy.com/lynis/
* NOTE / WARNING: This container is just for fun, and it works very poorly right now. Lynis doesnt have a --root-dir option, and Docker have a hard time mounting / as a volume.. So some dirty hacks just to get it going somehow to scan the host OS, not the docker container itself..

# Controll
* Build it: docker built -t tagname .
* Run: docker run -i -t -v /etc:/host_root/etc:ro -v /tmp:/host_root/tmp -v /homw:/host_root/home:ro -v /var:/host_root/var -v /root:/host_root/root:ro --rm tagname

# Info
* centos7 base image
