FROM centos:centos6

RUN yum install -y bind bind-utils

ADD start /start
RUN chmod 755 /start
ENTRYPOINT ["/bin/bash", "-e", "/start"]
CMD ["start"]

EXPOSE 53/udp
