* Original from https://github.com/nathanleclaire/wetty/blob/master/Dockerfile, but;

  * The original did a 'FROM node' which installs Debian. This one is on centos 7.
  * This one contains some more packages and more goodiness to act as a "first in line shell"
  * Replaced the login prompt, with a direct access to a shell (a root shell) as default.
  * Made an easy way to force a shell based on eg a script. (infoscreen-mode), if you like :)

NOTE: This version of wetty is ment to be placed behind your own secure reverse http(s) proxy.

# Running
* minimal: docker run -i -t -p 3000:3000 --rm xeor/wetty
* shell script(s) on login: `-v $PWD/start.sh:/etc/profile.d/start.sh`
  * You can have as many as you want
* Different login-shell: `-v $PWD/yourscript:/shell`
  * Usefull if you example want to force-run a shell script. Usefull for info-screens and so on.

# tips/trics
* Use it as is, play with and break it. It acts as a fullworthy CentOS 7 ( ehm, almost :) )
* Use it as a base-image, and mix it with a bunch of your own tools. Easy nmap/network-toolbox over web..
* Put it on a info-screen with some usefull terminal output. Using a Chrome tab-switcher to switch between tabs.
* Forced login to remote tmux session.
  * Generate a keypair, mounting the private key in the container as eg `/root/.ssh/id_rsa`, and the public part in whereever `authorized_keys` file you want to login to.
  * Mount up `/root/.ssh/known_hosts`
  * Make a simple shell with something like `ssh -t user@remote -- /bin/sh -c 'tmux has-session && exec tmux attach || exec tmux'`, and mount it as `/shell`
