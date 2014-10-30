# Info
* centos7 base image with EPEL
* Entrypoint script
* Used as a base for creating other containers
* In all images inheriting this one, you can set DEPENDING_ENVIRONMENT_VARS to a space separated list of required environment-variables.
* If there exits an ./init/setup file, it will be run on ENTRYPOINT
* If there exits an ./init/run-setup file, it will be run on no CMD or `run`
* You should add `COPY init/ /init/` to your Dockerfile with the right scripts in it. We wont use ONBUILD, since we coulnt leverage Dockers caching very good when changing init files

# Todo
* Add logging support to remote syslog. Define remote server as env
