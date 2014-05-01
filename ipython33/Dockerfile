FROM centos

RUN yum install -y centos-release-SCL
RUN yum install -y python33
RUN scl enable python33 'easy_install pip'
RUN scl enable python33 'pip install ipython'

CMD ["scl", "enable", "python33", "ipython"]

