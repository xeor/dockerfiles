FROM xeor/base-centos-daemon

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-10-06
ENV NGINX_VERSION 1.6.2

RUN yum install -y nginx wget tar python-setuptools && easy_install pip && pip install supervisor

RUN wget https://github.com/jwilder/docker-gen/releases/download/0.3.2/docker-gen-linux-amd64-0.3.2.tar.gz && \
    tar xvzf docker-gen-linux-amd64-0.3.2.tar.gz

ADD sites.tmpl /
ADD docker-gen.conf /
ADD nginx.conf /etc/nginx/nginx.conf

ENV DOCKER_HOST unix:///docker.sock
EXPOSE 80
