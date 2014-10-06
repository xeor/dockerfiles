FROM xeor/base-centos

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-10-02

RUN yum install -y supervisor && yum clean all
ONBUILD COPY supervisord.d/ /etc/supervisord.d/

COPY init/ /init/
