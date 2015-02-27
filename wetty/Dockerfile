FROM xeor/base-centos-daemon

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2015-02-26

RUN yum install -y git tar gcc-c++ nodejs make emacs-nox tmux
RUN curl https://www.npmjs.com/install.sh | clean=no sh
RUN git clone https://github.com/nathanleclaire/wetty.git && \
    cd wetty && \
    npm install

RUN sed 's@/bin/login@/bin/bash@' -i /wetty/app.js

COPY init/ /init/
COPY supervisord.d/ /etc/supervisord.d/

EXPOSE 3000

