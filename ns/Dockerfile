FROM xeor/base-alpine

ENV REFRESHED_AT 2017-03-01

RUN apk update \
    && apk add dnsmasq inotify-tools

COPY root /
