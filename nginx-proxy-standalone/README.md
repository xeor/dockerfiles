Based on https://github.com/jwilder/nginx-proxy but with some changes:

For a version of this with separation of the nginx daemon and the config generator, check out xeor/nginx-proxy-multi

* Centos base image
* Forces https and will redirect http with a 301. It will also set STS to 1 year.
* Using monit for startup
* Nginx from source, so its easier to customize and add modules
* Some minor nginx config tweeks
* Some path changes

# run (proxy) #
docker run -i -t -p 80:80 -p 443:443 -v /var/run/docker.sock:/docker.sock -v $PWD/certificates:/certificates xeor/nginx-proxy

# run (web-servers) #
Add VIRTUAL_HOST as an environment variables to them, and the proxy will detect them, add them and forward traffic to them..

# create self-signed certificates #
cd certificates
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -days 1825 -in server.csr -signkey server.key -out server.crt

