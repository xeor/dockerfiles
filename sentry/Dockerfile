FROM xeor/base-centos-daemon

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2015-01-13

RUN yum install -y postgresql postgresql-devel gcc libxslt-devel python-debug && \
    pip install python-decouple sentry[postgres]

COPY init/ /init/
COPY supervisord.d/ /etc/supervisord.d/

COPY sentry.conf.py /

VOLUME ["/data"]
EXPOSE 8080
