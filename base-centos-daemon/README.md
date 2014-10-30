# Usage
* Use this as the base image for your container
* Create a supervisord.d folder in the folder you have your Dockerfile, see ./supervisord.d/ for example services (they are only examples)
* Put setup code in ./init/setup, it will run at container start.
* Add `COPY supervisord.d/ /etc/supervisord.d/` to your Dockerfile and put all your supervisord *.ini files in that directory

# Environment
* `LOGLEVEL`: supervisord loglevel. Can be one of `debug`, `info`, `warn`, `error`, `critical`. Defaults to `error`
* `DEPENDING_ENVIRONMENT_VARS` (from base-centos): Set to a list of variables that needs to be defined for the container to run.
