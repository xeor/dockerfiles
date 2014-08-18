NOT DONE

Based on https://github.com/jwilder/nginx-proxy but with some changes:

* centos base image
* monit
* nginx from source
* separation of docker-gen and nginx container (TODO)
* some path changes

# run #
docker run -i -t -p 80:80 -v /var/run/docker.sock:/docker.sock ... bash
