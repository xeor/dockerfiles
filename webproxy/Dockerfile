FROM centos:centos7

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-09-21
ENV NGINX_VERSION 1.4.4

RUN yum localinstall -y http://dl.fedoraproject.org/pub/epel/beta/7/x86_64/epel-release-7-1.noarch.rpm
RUN yum install -y nginx wget tar python-setuptools && easy_install pip && pip install supervisor

RUN wget https://github.com/jwilder/docker-gen/releases/download/0.3.2/docker-gen-linux-amd64-0.3.2.tar.gz && \
    tar xvzf docker-gen-linux-amd64-0.3.2.tar.gz

ADD sites.tmpl /
ADD supervisord.conf /
ADD docker-gen.conf /
ADD nginx.conf /etc/nginx/nginx.conf

ADD start /start
RUN chmod 755 /start
ENTRYPOINT ["/bin/bash", "-e", "/start"]
CMD ["start"]

ENV DOCKER_HOST unix:///docker.sock
EXPOSE 80
