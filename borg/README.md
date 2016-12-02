# Borgbackup docker image

This is a lightweight (based on alpine) docker container image for borgbackup.
It's goal is to include everything needed to run borgbackup, as a server, and
as a client.


## Usage

command="borg serve --append-only --restrict-to-path /path/to/repo",no-pty,no-agent-forwarding,no-port-forwarding,no-X11-forwarding,no-user-rc ssh-rsa AAAAB3[...]

borg init ssh://root@127.0.0.1:2222/data/b
