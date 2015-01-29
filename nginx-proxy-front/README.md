This container is ment as a web-front when you dont have more than 1 ip-address available and can route web domains to spesific ips and from there to containers.
It will based on mounted configuration forward requests to another port/ip:port. From there, you can use another proxy to forward it on to the web-server container.

* Forces https and will redirect http with a 301. It will also set STS to 1 year.
  * Mainly so we dont haveto deal with two ports forwarding, and because ssl certs are cheap (https://cheapsslsecurity.com), (and soon free, (https://letsencrypt.org/)).

# run 
docker run -i -t -p 80:80 -p 443:443 -v $PWD/domains:/domains xeor/nginx-proxy-front

# configuration
Put 1 folder per domain (vhost), inside the `./domains/` folder in the format `domain_remote[:port]`, with one `server.pem`, and `server.key` in.
The container watches this folder, so if you add a domain, it will be included without you having to restart the container.

* If want this proxy for localhost, you will need to use `--net host` when starting the container..
* Let this container take care of ssl, so the ports you proxy to, should be NON ssl...


To create a test self-signed certificate pair; `openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.pem -days 3650 -nodes`
