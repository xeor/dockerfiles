# Borgbackup docker image

This is a lightweight (based on alpine) docker container image for borgbackup.
It's goal is to include everything needed to run borgbackup, as a server, and
as a client.


## Usage - server

There are a couple of directores that we should mount inside the running container.

*   `/data`: A good name/folder to store your backups. You can really use whatever name you
             want on this folder, as long as you tell borg.

*   `/root`: At least, mount up `/root/.ssh`, or the `authorized_keys` file. You
             should prepend your entry in the authorized_keys with something like;
             `command="borg serve --append-only --restrict-to-path /data",no-pty,no-agent-forwarding,no-port-forwarding,no-X11-forwarding,no-user-rc ssh-rsa AAAAB3...`
             Or skip the `--append-only`. See options [here](https://borgbackup.readthedocs.io/en/stable/usage.html#borg-serve).

*   `/etc/ssh/hostkeys`: We store the ssh identity files here. Mount it to keep the same sshd
                         identity between starts.

## Usage - client (untested, but should work)

You can use this docker image as a client as well, but having borg in a docker container
might feel weird. When creating a backup, you define a set of paths to backup. Paths that
we need to mount.
Use the included `borg` script to start borg inside the image. You must also set
your docker mountpoints in the file `${HOME}/.config/borg/docker-client.conf`.
The content of that file is made into 1 line, and added as additional docker parameters.

This might or might not work as you want.. You should really use your os version of the borg client,
not the one in this image (even tho it's fresh from pip and contains the needed libs).

To talk to a borg server that is not on port 22, use something like this;
`borg init ssh://root@127.0.0.1:2222/data/important`

Check out the [environment variable section](https://borgbackup.readthedocs.io/en/stable/usage.html#environment-variables)
in the documentation for some tips of what you can set using `-e`.

Look [here](https://borgbackup.readthedocs.io/en/stable/usage.html#borg-help-patterns) for info
about pattern-matching.

## Example usage
```sh
# Initialize archive
borg init -e keyfile -a -v ssh://root@10.1.2.3/data/desktop

# Make .no-regular-backup files in the folders you want to skip. Easier than --excluding them all..
touch Temp/.no-regular-backup

# Run regulary
borg create -v -s -p "ssh://root@10.1.2.3/data/desktop::{hostname}-medium-{now:%Y-%m-%d_%H:%M:%S}" \
  --exclude-if-present=.no-regular-backup \
  --exclude '*.pyc' --exclude '*/.apm' --exclude '*/.npm' --exclude '*/.gem' --exclude '*/.node-gyp' \
  --exclude '*/node_modules' --exclude '*/site-packages' --exclude '*/.Trash' --exclude '*/compile-cache' --exclude '*/*_old' \
  /Users/username

# Run once in a while
borg create -v -s -p "ssh://root@10.1.2.3/data/desktop::{hostname}-big-{now:%Y-%m-%d_%H:%M:%S}" \
 --exclude-if-present=.no-backup \
 --exclude '*.pyc' --exclude '*/node_modules' --exclude '*/.Trash' \
 /Users/username /private/etc/
```

## TODO
*   Use a `backup` user inside the container, not `root`
