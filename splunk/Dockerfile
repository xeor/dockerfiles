FROM xeor/base-centos-daemon

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-10-07

# inotify-tools isnt in epel stable yet... (2014-10-07)
RUN yum install -y --enablerepo=epel-testing dnsmasq inotify-tools

COPY splunk.rpm /
RUN yum localinstall -y /splunk.rpm && chown splunk: /opt/splunk

USER splunk

EXPOSE 8000 9997
