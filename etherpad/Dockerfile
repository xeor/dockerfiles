FROM xeor/base-centos-daemon

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-10-06
ENV DEPENDING_ENVIRONMENT_VARS POSTGRESQL_PORT

# FIXME: Abiword package not currently in http://li.nux.ro/download/nux/dextop/el7/x86_64/ (2014-10-06)

RUN yum localinstall -y http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm && \
#    yum install -y abiword && \
    yum install -y --enablerepo=centosplus npm git openssl-devel which tar postgresql-devel make && \
    yum clean all

RUN git clone --progress --verbose https://github.com/ether/etherpad-lite.git && \
    cd etherpad-lite && \
    sh /etherpad-lite/bin/installDeps.sh && \
    npm install ep_list_pads ep_public_view

ADD settings.json /etherpad-lite/

EXPOSE 8080
