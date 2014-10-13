pydio (AjaXplorer) - https://pyd.io

The point of this pydio is for personal use. Pydio support very large installations, but the meaning of this container is to use it for your home-needs.

There is a trusted docker-build made from (https://github.com/pydio/pydio-core/tree/develop/dist/docker) which is from upsteam the reason I made this is:
* It did not work
* It had many build-steps
* Wanted to use my own template for supervisord containers
* Wanted centos7
* Run as non-root behind port 8080
* No sshd
* No database..
* No SSL, as this will be done by a reverse proxy

# todo
* Warnings/Errors at installation
  * Missing "Server charset encoding"
* Clever way to mount /data, copy/symling /pydio/data if exists, or something to get a persistent install..
* php extensions for different plugins
* Authentication based on HTTP_USER
* Cleanup

# run
docker run -d -v ${PWD}/data:/pydio/data xeor/pydio
