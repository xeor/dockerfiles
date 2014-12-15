FROM xeor/base-centos

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-12-15

RUN yum install -y python-pip && yum clean all && \
    pip install supervisor

COPY init/ /init/
