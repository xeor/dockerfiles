FROM xeor/base-alpine:0.4

LABEL maintainer="Lars Solberg <lars.solberg@gmail.com>"

ENV REFRESHED_AT="2018-02-18" \
    PYTHONIOENCODING="utf-8"

RUN apk add --no-cache python3 \
    && pip3 install taggo

COPY root /

