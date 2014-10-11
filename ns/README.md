Quick and dirty dnsmasq container.

# todo
* ad-block function
  * http://hosts-file.net/.%5Cad_servers.txt
  * http://pgl.yoyo.org/adservers/serverlist.php?hostformat=dnsmasq&showintro=0&mimetype=plaintext
  * http://winhelp2002.mvps.org/hosts.txt

# run
docker run -d -v /path/to/dnsmasq/configs:/etc/dnsmasq.d -p 53:53/udp xeor/ns
