Quick and dirty dnsmasq container.

# run #
docker run -d -v /path/to/dnsmasq/configs:/etc/dnsmasq.d -p 53:53/udp xeor/ns
