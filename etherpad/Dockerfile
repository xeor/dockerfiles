FROM centos:centos6

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-08-21

RUN yum install -y https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

RUN yum install -y --enablerepo=centosplus nodejs git openssl-devel which tar
RUN curl https://www.npmjs.org/install.sh | clean=no sh

RUN git clone --progress --verbose https://github.com/ether/etherpad-lite.git && \
    cd etherpad-lite && \
    sh /etherpad-lite/bin/installDeps.sh

ADD settings.json /etherpad-lite/
ADD default_pad.txt /

ADD start /start
RUN chmod 755 /start
ENTRYPOINT ["/bin/bash", "-e", "/start"]
CMD ["start"]

EXPOSE 80
