FROM centos:centos7

MAINTAINER Lars Solberg <lars.solberg@gmail.com>

RUN yum localinstall -y http://dl.fedoraproject.org/pub/epel/beta/7/x86_64/epel-release-7-0.2.noarch.rpm
RUN yum install -y git tar gcc-c++ nodejs make emacs-nox tmux
RUN curl https://www.npmjs.org/install.sh | clean=no sh
RUN git clone https://github.com/nathanleclaire/wetty.git && \
    cd wetty && \
    npm install

RUN useradd -d /home/term -m -s /bin/bash term
RUN echo 'term:term' | chpasswd

# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=966807 (also happens on debian)
RUN sed -e '/^session[ ]*required[ ]*pam_loginuid\.so$/s/^/#/g' -i /etc/pam.d/login

EXPOSE 3000

WORKDIR /wetty
CMD ["node", "app.js", "-p", "3000"]
