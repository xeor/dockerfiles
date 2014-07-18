* Original from https://github.com/nathanleclaire/wetty/blob/master/Dockerfile
** The original did a 'FROM node' which installs Debian. This one is on centos
** This one contains some more packages and more customized things.
** Fix for pam bug that affected both debian and centos and made it impossible to login

# Controll
* Build it: docker built -t tagname .
* Run: docker run -i -t -p 3000:3000 --rm tagname

# Info
* centos7 base image
