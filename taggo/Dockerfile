FROM xeor/base:7.1-2

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2015-11-13

# Force python3's stdin/stdout encoding to be utf-8, instead of guessing..
ENV PYTHONIOENCODING utf-8

COPY init/ /init/
COPY hooks/ /hooks/
RUN chmod +x /hooks/*
COPY supervisord.d/ /etc/supervisord.d/

# Taggo
RUN yum install -y git inotify-tools && \
    git clone https://github.com/xeor/taggo.git && \
    yum clean all
COPY taggo-default.cfg /taggo-default.cfg
