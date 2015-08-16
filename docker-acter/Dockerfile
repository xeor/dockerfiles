FROM xeor/base-centos

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2015-08-15

RUN yum install -y python-pip && pip install docker-py

COPY worker.py /
RUN chmod +x /worker.py

COPY runners/ /runners
RUN chmod +x /runners/*

CMD ["/worker.py"]
