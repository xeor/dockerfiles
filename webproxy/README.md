Simple nginx reverse proxy that will proxy every container with HTTP_PROXY_PATH sat to http://.../HTTP_PROXY_PATH
This container was born because of the need of internal services talking to eachothers without going trough the wwwhisper container which needs authentication.
You can also set HTTP_PROXY_PORT if the port is not :80

# Run #

Start the container with something like:

    docker run -d -p 80:80 -v /var/run/docker.sock:/docker.sock xeor/webproxy

This container will detect the new container and automaticly do whats needed.
