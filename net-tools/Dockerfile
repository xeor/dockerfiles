FROM centos:centos7

MAINTAINER Lars Solberg <lars.solberg@gmail.com>

RUN yum localinstall -y http://dl.fedoraproject.org/pub/epel/beta/7/x86_64/epel-release-7-0.2.noarch.rpm

RUN yum install -y curl wget tmux tar unzip \
                   iputils net-tools bind-utils nmap nc iptraf-ng mtr tcpdump

CMD ["bash", "-l"]
