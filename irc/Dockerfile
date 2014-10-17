FROM xeor/base-centos

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-10-16

# General (might be dependencies only 1 need here, but still felt general..)
RUN yum install -y tmux git tar cmake gcc gcc-c++ make && \
    useradd irc

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

#USER irc

