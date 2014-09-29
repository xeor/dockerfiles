More info @ https://github.com/wrr/wwwhisper

Simple nginx reverse proxy that hides container services that is linked on port 80 behind protected areas..

# Run #

Start the container with something like:

    docker run -d -e "SITE_URL=http://admin.your.domain" -e "ADMIN_MAIL=your@mail.com" -p 80:80 -v /var/run/docker.sock:/docker.sock xeor/wwwhisper

For each container you want exposed under admin.your.domain/here, run the other containers with example `-e WWWHISPER_PROTECT=here` to expose the containers port 80 under that location.
This wwwhisper container will detect the new container and automaticly do whats needed.

If you want to keep your settings after container exit, mount the data volume on your host with something like `-v datadir-on-host:/wwwhisper/sites`

# admin #
Is available via /wwwhisper/admin/

