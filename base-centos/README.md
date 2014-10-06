# Info
* centos7 base image with EPEL
* Entrypoint script
* Used as a base for creating other containers
* In all images inheriting this one, you can set DEPENDING_ENVIRONMENT_VARS to a space separated list of required environment-variables.
* If there exits an ./init/setup file, it will be run on ENTRYPOINT
* If there exits an ./init/run-setup file, it will be run on no CMD or `run`
