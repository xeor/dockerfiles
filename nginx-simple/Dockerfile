FROM xeor/base-centos-daemon

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2015-02-07

RUN yum install -y nginx inotify-tools

COPY init/ /init/
COPY supervisord.d/ /etc/supervisord.d/
COPY nginx-global.conf /etc/nginx/nginx.conf

