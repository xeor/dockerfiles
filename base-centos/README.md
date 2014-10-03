# Info
* centos7 base image with EPEL
* Entrypoint script
* Used as a base for creating other containers

# Usage
* Create a supervisord.d folder in the folder you have your Dockerfile, see ./supervisord.d/ for example services (they are only examples)

# Environment
* `LOGLEVEL`: supervisord loglevel. Can be one of `debug`, `info`, `warn`, `error`, `critical`. Defaults to `error`
