FROM xeor/base-centos-daemon

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-10-03

# inotify-tools isnt in epel stable yet... (2014-10-03)
RUN yum install -y --enablerepo=epel-testing dnsmasq inotify-tools

COPY supervisord.d/ /etc/supervisord.d/

ADD dnsmasq.conf /etc/dnsmasq.conf
