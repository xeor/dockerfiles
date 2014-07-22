* Lynis is a free and opensource auditing tool from Cisofy (with an enterprise brother), located at http://cisofy.com/lynis/

# Controll
* Build it: docker built -t tagname .
* Run: docker run -i -t -v /etc:/host_root/etc:ro -v /tmp:/host_root/tmp -v /homw:/host_root/home:ro -v /var:/host_root/var -v /root:/host_root/root:ro --rm tagname

# Info
* centos7 base image
