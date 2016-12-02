FROM xeor/base-alpine
MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2016-11-20
EXPOSE 22
VOLUME ["/data", "/root", "/etc/ssh/hostkeys"]

# Using py3-msgpack@edge instead of pip install msgpack because the PiPY version
# is not optimized (it's pure python).

RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && apk update \
    && apk add --no-cache fuse libacl libattr lz4 openssl pkgconfig python3 openssh py3-msgpack@edge \
    && apk add --no-cache --virtual .build-deps acl-dev attr-dev fuse-dev gcc lz4-dev musl-dev openssl-dev python3-dev \
    && pip3 install borgbackup llfuse \
    && apk del .build-deps \
    && rm -f /etc/ssh/ssh_host_*

COPY root /
