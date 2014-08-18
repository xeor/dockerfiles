Based on https://github.com/jwilder/nginx-proxy but with some changes:

* Separation of docker-gen and nginx container (for a standalone version, check out xeor/nginx-proxy-standalone)
* Centos base image
* Forces https and will redirect http with a 301. It will also set STS to 1 year.
* Uses default CMD/ENTRYPOINT for startup, since the containers are simplefied
* Nginx from source, so its easier to customize and add modules
* Some minor nginx config tweeks
* Some path changes

Note that the location of the certificates is in the same folder as the README.md file. Not in the containers folder.
You will need to provide a server.crt and a server.key file.

# nginx-proxy-forwarder #
This is the container with nginx. This needs to read some of its nginx configuration from the nginx-proxy-watcher.
If it sees that the dynamic nginx config have been changed, it will reload the nginx daemon.
To run it, you will need something like:

    docker run -i -t -p 80:80 -p 443:443 --volumes-from=nginx-proxy-watcher -v $PWD/certificates:/certificates xeor/nginx-proxy-forwarder

# nginx-proxy-watcher #
This is the container in charge of generating the dynamic nginx configuration we the other container uses. It shares this over a volume.
To do this, it needs access to the docker.sock file, and thats why we separate this containers.
To run it, you need something like:

    docker run -i -t -v /var/run/docker.sock:/docker.sock --name=nginx-proxy-watcher xeor/nginx-proxy-watcher

# The other containers with web resources #
To add a virtual host, just add VIRTUAL_HOST as an environment variables to the containers you want shared and the proxy will detect them and start sending traffic to them if the domain matches..

# create self-signed certificates #
cd certificates
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -days 1825 -in server.csr -signkey server.key -out server.crt

