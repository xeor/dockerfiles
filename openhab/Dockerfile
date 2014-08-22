FROM centos:centos6

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-08-22

# EPEL packages
RUN yum install -y https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum install -y tmux wget unzip java-1.7.0-openjdk

RUN cd /srv && \
    wget https://github.com/openhab/openhab/releases/download/v1.5.0/distribution-1.5.0-runtime.zip && unzip distribution-1.5.0-runtime.zip && \
    cd /srv/addons && \
    wget https://github.com/openhab/openhab/releases/download/v1.5.0/distribution-1.5.0-addons.zip && unzip distribution-1.5.0-addons.zip

# https://github.com/cdjackson/HABmin
RUN cd /srv && \
  wget https://github.com/cdjackson/HABmin/releases/download/0.1.3-snapshot/habmin.zip && unzip habmin.zip

# Debugging tool (MinOZW /dev/zwave)
RUN yum localinstall -y \
  http://mirror.my-ho.st/Downloads/OpenZWave/CentOS_CentOS-6/x86_64/libopenzwave-1.0.791-2.1.x86_64.rpm \
  http://mirror.my-ho.st/Downloads/OpenZWave/CentOS_CentOS-6/x86_64/openzwave-1.0.791-2.1.x86_64.rpm


RUN cp /usr/share/zoneinfo/Europe/Oslo /etc/localtime

# Misc temporary fixes
#RUN rm -f /srv/addons/org.openhab.binding.zwave-1.5.0-SNAPSHOT.jar

## Handeled by host udev rules since docker wont run udev inside container
# ADD etc/udev/rules.d/99-zwave.rules /etc/udev/rules.d/99-zwave.rules
# RUN for i in /dev/ttyUSB*; do udevadm test $(udevadm info --query path --name $i); done

ADD start /start
RUN chmod 755 /start
ENTRYPOINT ["/bin/bash", "-e", "/start"]
CMD ["start"]

EXPOSE 8080
