* sickbeard container for general use
* Start with something like: `docker run -d -v $PWD/config.ini:/sickbeard/config.ini -p 8081:8081 xeor/sickbeard`
* Note that the config.ini file is generated at first start, so there is no Docker environment variable to set to configure stuff like base-url
