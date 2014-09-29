* Misc docker containers made for private use, but might be useful for others :)

# Debugging
* nsenter (and the alias docker-enter): Install with 'docker run --rm -v /usr/local/bin:/target jpetazzo/nsenter', and use 'nsenter containerID' to get in

# Other usefull containers
* docker run -t -i linux/kali-metasploit (https://registry.hub.docker.com/u/linux/kali-metasploit/)
* squid in a can (usefull for caching)
** info: https://github.com/jpetazzo/squid-in-a-can
** run: docker run --net host -d -v $PWD/data:/var/spool/squid3 jpetazzo/squid-in-a-can
** run: iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to 3129
* https://github.com/jpetazzo/critmux
