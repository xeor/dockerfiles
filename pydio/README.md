pydio (AjaXplorer) - https://pyd.io

The point of this pydio is for personal use. Pydio support very large installations, but the meaning of this container is to use it for your home-needs.

There is a trusted docker-build made from (https://github.com/pydio/pydio-core/tree/develop/dist/docker) which is from upsteam the reason I made this is:
* It did not work
* It had many build-steps
* Wanted to use my own template for supervisord containers
* Wanted centos7
* Run as non-root behind port 8080
* No sshd
* No database.. (but sqlite support is in)
* No SSL, as this will be done by a reverse proxy
* Many libs for using the different plugins.

# todo
* Warnings/Errors at installation
  * Missing "Server charset encoding"

# run
* docker run -d -v ${PWD}/pydio_data:/data xeor/pydio
  * To mount other directores, use something other than /data. /data is for all the pydio configuration (if you want it persistant).
