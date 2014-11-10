FROM xeor/base-centos-daemon

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-11-10

# Force python3's stdin/stdout encoding to be utf-8, instead of guessing..
ENV PYTHONIOENCODING utf-8

ENV IPYTHONDIR /data/.ipython

VOLUME ["/data"]
EXPOSE 8888

COPY init/ /init/
COPY supervisord.d/ /etc/supervisord.d/

COPY requirements.txt /

RUN yum install -y gcc gcc-c++ zeromq3-devel freetype-devel libpng-devel && \
    yum localinstall -y https://www.softwarecollections.org/en/scls/rhscl/python33/epel-7-x86_64/download/rhscl-python33-epel-7-x86_64.noarch.rpm && \
    yum install -y scl-utils python33 && \
    scl enable python33 'easy_install pip' && \
    scl enable python33 'pip install -r /requirements.txt' && \
    yum clean all

