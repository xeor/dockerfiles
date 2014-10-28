Gets logs (stdout) from all the Docker containers on the hosts and sends it to Splunk

* Built with CentOS 7 base-image
* Using docker-gen (https://github.com/jwilder/docker-gen) and the fluentd example
* Using Fluentd Splunk plugin (https://github.com/parolkar/fluent-plugin-splunk)
* This container is kinda Splunk locked-down. But it is very easy to steal the Dockerfile if you need anything else..

# run
* Run with something like `docker run -d -e "SPLUNK_HOST=splunked" -e "SPLUNK_PORT=514" -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker/containers:/var/lib/docker/containers xeor/splogger`
* Fluentd runs in daemon mode so we wont get any feed-back loop..

# env
* `SPLUNK_HOST`: Splunk host to send to
* `SPLUNK_PORT`: The splunk port to send to

