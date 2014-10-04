Based on https://github.com/jwilder/nginx-proxy but with some changes:

* Separation of docker-gen and nginx container (for a standalone version, check out xeor/nginx-proxy-standalone)
* Centos base image
* Forces https and will redirect http with a 301. It will also set STS to 1 year.
* Uses default CMD/ENTRYPOINT for startup, since the containers are simplefied
* Nginx from source, so its easier to customize and add modules
* Assume you are using a real certificate and not a self-signed. Not a big config change, but this readme and nginx.tmpl assumes a .pem instead of .crt
* Some minor nginx config tweeks
* Some path changes

Note that the location of the certificates is in the same folder as the README.md file. Not in the containers folder.
You will need to provide a server.crt and a server.key file.

# nginx-proxy-forwarder #
This is the container with nginx. This needs to read some of its nginx configuration from the nginx-proxy-watcher.
If it sees that the dynamic nginx config have been changed, it will reload the nginx daemon.
To run it, you will need something like:

    docker run -i -t -p 80:80 -p 443:443 --volumes-from=nginx-proxy-watcher -v $PWD/certificates:/certificates xeor/nginx-proxy-m-forwarder

# nginx-proxy-watcher #
This is the container in charge of generating the dynamic nginx configuration we the other container uses. It shares this over a volume.
To do this, it needs access to the docker.sock file, and thats why we separate this containers.
To run it, you need something like:

    docker run -i -t -v /var/run/docker.sock:/docker.sock --name=nginx-proxy-watcher xeor/nginx-proxy-m-watcher

Note that you will need to add `--privileged=true` if you want to mount docker.sock like this when SELinux is enforcing..

# The other containers with web resources #
To add a virtual host, just add VIRTUAL_HOST as an environment variables to the containers you want shared and the proxy will detect them and start sending traffic to them if the domain matches..

# ssl certificates #
## For real
* cd certificates
* openssl genrsa -out server.key 2048
* openssl req -new -key server.key -out server.csr
* // submit server.csr to a certificate authority and they will probably send you a .pem bundle back.
* // Rename the .pem to server.pem and put it in the same directory

## For test
* cd certificates
* openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.pem -days 3650 -nodes
