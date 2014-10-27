* Container that talks to SickBeard, asks for shows that starts with `NRK - `, take the showname and downloads it from NRK.
* Start with something like: `docker run -d -v $PWD/download:/download xeor/nrk-sb-ripd`

# env
* `SICKBEARD_URL`: Sickbeard url
* `SICKBEARD_API_KEY`: Api key. Remember to enable this in Sickbeard settings
