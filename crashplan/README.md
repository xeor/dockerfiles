This is a Crashplan (https://www.code42.com/crashplan/) container running both the Crashplan daemon, and the graphical java-ui (which you can connect to via VNC).

The first time you start it, make sure you mount up the data folder so you don't haveto setup Crashplan every time.
Connect via VNC to do the setup.

To use VNC over an ssh-tunell do something like `ssh -nNT -L 5555:localhost:5900 docker@dockerhost` then connect to vnc on `localhost:5555`.
The default vnc password is `secret` but you might change that setting the `vncpass` environment variable when starting the container.
