FROM xeor/base-centos-daemon

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-12-23

RUN yum install -y nginx git rubygems ruby-devel gcc tar patch libxml2-devel make

COPY generatord.sh /
RUN gem install git_stats && chmod +x /generatord.sh

COPY nginx.conf /etc/nginx/conf.d/git-stats.conf
COPY init/ /init/
COPY supervisord.d/ /etc/supervisord.d/

VOLUME ["/data"]
EXPOSE 8080
