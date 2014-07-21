FROM centos:centos7

MAINTAINER Lars Solberg <lars.solberg@gmail.com>

RUN yum localinstall -y http://dl.fedoraproject.org/pub/epel/beta/7/x86_64/epel-release-7-0.2.noarch.rpm

RUN yum install -y strace curl wget vim emacs-nox diffstat tmux \
                   git mercurial subversion \
                   tar unzip make

# Python stuff
ADD requirements.txt ./
RUN yum install -y python-setuptools && \
    easy_install pip && \
    pip install -r /requirements.txt

# npm
RUN yum install -y nodejs
RUN curl https://www.npmjs.org/install.sh | clean=no sh

# Other customizations
RUN mkdir /data
RUN mkdir /setup

## Ninjab (the prompt)
RUN cd /setup && \
    git clone https://github.com/xeor/ninjab.git && \
    echo '. /setup/ninjab/loader' >> /.profile

VOLUME /data
WORKDIR /data

ADD start /start
RUN chmod +x /start
ENTRYPOINT ["/start"]
CMD ["bash", "-l"]

