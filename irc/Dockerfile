FROM xeor/base-centos

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-10-16

# General (might be dependencies for stuff below, but still felt general..)
RUN yum install -y tmux git tar cmake gcc gcc-c++ make && \
    useradd -d /home/irc -m -s /bin/bash irc && \
    echo '[[ $TMUX ]] || tmux attach' >> /home/irc/.bashrc

# SSH (include init.d patch so sshd-keygen wont get errors)
RUN yum install -y openssh-server && \
    echo 'success() { echo "${1}"; }; failure() { echo "${1}"; }' > /etc/rc.d/init.d/functions && \
    /usr/sbin/sshd-keygen 

# WeeChat
RUN yum install -y gettext libgcrypt-devel gnutls-devel libcurl-devel ncurses-devel perl \
                   python-devel perl-ExtUtils-Embed perl-devel ruby-devel lua-devel tcl-devel && \
    curl -L http://weechat.org/files/src/weechat-1.0.1.tar.gz > weechat.tgz && \
    tar -zxvf weechat.tgz && mv weechat-* weechat-build && cd weechat-build && \
    mkdir build && cd build && cmake .. && make && make install && cd / && \
    rm -rf weechat.tgz weechat-build && yum clean all

# Glowing Bear
RUN yum install -y nginx && \
    git clone https://github.com/glowing-bear/glowing-bear && \
    rm -rf /usr/share/nginx/html && ln -s /glowing-bear /usr/share/nginx/html

# Wetty
RUN yum install -y nodejs && \
    curl https://www.npmjs.org/install.sh | clean=no sh && \
    git clone https://github.com/nathanleclaire/wetty.git && \
    cd wetty && npm install && \
    sed -e '/^session[ ]*required[ ]*pam_loginuid\.so$/s/^/#/g' -i /etc/pam.d/login && \
    sed "s/term = pty.spawn('\/bin\/login.*/term = pty.spawn('\/usr\/bin\/su', ['irc', '-c', '\/bin\/bash', '-l'], {/" -i /wetty/app.js

# BitlBee
RUN yum install -y glib2-devel libotr-devel libpurple-devel && \
    curl -L http://get.bitlbee.org/src/bitlbee-3.2.2.tar.gz > bitlbee.tgz
    tar -zxvf bitlbee.tgz && mv bitlbee-* bitlbee-build && cd bitlbee-build && \
    ./configure --otr=1 --purple=1 && make && make install && make install-etc

COPY init/ /init/

#USER irc
