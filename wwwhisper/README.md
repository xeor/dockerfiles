More info @ https://github.com/wrr/wwwhisper

Simple nginx reverse proxy that hides container services that is linked on port 80 behind protected areas..

# Run #

Start the container with something like:

    docker run -d -e "SITE_URL=http://admin.your.domain" -e "ADMIN_MAIL=your@mail.com" -p 80:80 -v /var/run/docker.sock:/docker.sock xeor/wwwhisper

For each container you want exposed under admin.your.domain/here, run the other containers with example `-e WWWHISPER_PROTECT=here` to expose the containers port 80 under that location.
This wwwhisper container will detect the new container and automaticly do whats needed.

If you want to keep your settings after container exit, mount the data volume on your host with something like `-v datadir-on-host:/wwwhisper/sites`

# Environment variables possible on "clients" #
* `WWWHISPER_PROTECT`: Set to the "folder" you want the request to be forwarded to. Example `git` for your.site.com/git/
* `WWWHISPER_PORT`: If the port you are using on the web-server is not 80, you can set it manually.
* `WWWHISPER_USES_RELATIVE_PATH`: Set to `true` if the backend web-server needs the request to come in like your.site.com/api/endpoint, instead of your.site.com/git/api/endpoint. This is useful if there is no way to set the relative path on the backend application and it uses relative paths (like `../static/main.js`) to request its resources.

# admin #
Is available via /wwwhisper/admin/

