* sabnzbd container for general use
* Start with something like: docker run -d -v ${PWD}/config:/.sabnzbd -v ${PWD}/downloads:/Downloads -p 8080 xeor/sabnzbd
* There is no environmentvariables to set. The sabnzbd configuration is generated first via a web wizard. So there is nothing for `Docker` to do, and I dont wanted to provide a default one.
