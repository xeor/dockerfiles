FROM centos:centos6

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-09-28

RUN yum localinstall -y https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm && \
    yum localinstall -y http://li.nux.ro/download/nux/dextop/el6/x86_64/nux-dextop-release-0-1.el6.nux.noarch.rpm && \
    yum install -y abiword && \
    yum install -y --enablerepo=centosplus npm git openssl-devel which tar postgresql-devel && \
    yum clean all

RUN git clone --progress --verbose https://github.com/ether/etherpad-lite.git && \
    cd etherpad-lite && \
    sh /etherpad-lite/bin/installDeps.sh && \
    npm install ep_list_pads ep_public_view

ADD settings.json /etherpad-lite/

ADD start /start
RUN chmod 755 /start
ENTRYPOINT ["/bin/bash", "-e", "/start"]
CMD ["start"]

EXPOSE 8080
