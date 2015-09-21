FROM xeor/base-centos-daemon
MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2015-09-17

EXPOSE 8080

COPY supervisord.d/ /etc/supervisord.d/
COPY init/ /init/

RUN pip install --upgrade pip && \
    yum install -y gcc python-devel git && \
    pip install buildbot buildbot-slave
