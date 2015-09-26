This container is ment as a web-front when you dont have more than 1 ip-address available and can route web domains to spesific ips and from there to containers.
It will based on mounted configuration forward requests to another port/ip:port. From there, you can use another proxy to forward it on to the web-server container.

* Forces https and will redirect http with a 301. It will also set STS to 1 year.
  * Mainly so we dont haveto deal with two ports forwarding, and because ssl certs are cheap (https://cheapsslsecurity.com), (and soon free, (https://letsencrypt.org/)).

# run 
docker run -i -t -p 80:80 -p 443:443 -v $PWD/domains:/domains xeor/nginx-proxy-front

# configuration
Put 1 folder per domain (vhost), inside the `./domains/` folder in the format `domain_remote[:port]`, with one `server.pem` (or `.crt`), and `server.key` in.
The container watches this folder, so if you add a domain, it will be included without you having to restart the container.

* If want this proxy for localhost, you will need to use `--net host` when starting the container..
* Let this container take care of ssl, so the ports you proxy to, should be NON ssl/tls...
* See the generator.sh file for what it supports :)

# certificates
* example with cheapssl
  * generate request: `openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr`
  * Use it @ https://cheapsslsecurity.com
  * bundle up server.crt from the zip they sends you: `cat your_domain_com.crt COMODORSA* AddTrustExternalCARoot.crt > server.crt`
    * https://cheapsslsecurity.com/blog/install-ssl-certificate-nginx-http-server/
  * Use the `server.crt` file with the `server.key` file in your `domains` folder.
* self-signed (testing): `openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.pem -days 3650 -nodes`
