FROM centos:centos6

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-08-27

#RUN yum install -y https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum install -y wget
RUN wget -O so.rpm "https://spideroak.com/getbuild?platform=fedora&arch=x86_64" && yum localinstall -y so.rpm

ADD start /start
RUN chmod 755 /start
ENTRYPOINT ["/bin/bash", "-e", "/start"]
CMD ["start"]
