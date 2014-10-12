FROM xeor/base-centos-daemon

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-10-12

#RUN yum localinstall -y http://dl.ajaxplorer.info/repos/pydio-release-1-1.noarch.rpm && \
#    yum --disablerepo=pydio-testing install pydio


ADD nginx.conf /etc/nginx/conf.d/pydio.conf

# There is a Docker/centos7 bug that makes the httpd installation fail, but we are using nginx anyway, so that is why we are eating up the failed yum command..
RUN yum install -y unzip php php-fpm php-xml php-pdo sqlite nginx || true && \
    curl -L http://sourceforge.net/projects/ajaxplorer/files/pydio/stable-channel/5.2.3/pydio-core-5.2.3.zip/download > pydio.zip && \
    unzip pydio.zip && mv pydio-core* pydio && \
    sed '/^listen = /clisten = 0.0.0.0:9000' -i /etc/php-fpm.d/www.conf && \
    sed '/^upload_max_filesize = /cupload_max_filesize = 1G' -i /etc/php.ini && \
    chown -R apache: /pydio/data 
    




#RUN yum localinstall -y http://dl.ajaxplorer.info/repos/el6/pydio-stable/pydio-5.2.3-1.noarch.rpm && \
#    yum localinstall -y http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \
#    curl http://www.atomicorp.com/installers/atomic | sh && \
#    yum install -y httpd php-mcrypt* ImageMagick ImageMagick-devel \
#                   ImageMagick-perl gcc cc php-pecl-apc php php-mysql \
#                   php-cli php-devel php-gd php-pecl-memcache php-pspell \
#                   php-snmp php-xmlrpc php-xml php-imap mod_ssl openssl \
#                   mysql-server mysql php-ioncube-loader

#RUN chmod 0777 /etc/create.mysql && \
#    chmod +x /etc/gencert.sh && \
#    chmod +x /etc/pre_conf_pydio.sh && \
#    chmod +x /etc/configure_php_modules.sh


#RUN /etc/gencert.sh
#RUN /etc/configure_php_modules.sh
#RUN echo -e "NETWORKING=yes" > /etc/sysconfig/network
#RUN yum install -y pydio
#RUN /etc/pre_conf_pydio.sh
#RUN yum install -y python-pip && pip install "pip>=1.4,<1.5" --upgrade
#RUN pip install supervisor
#VOLUME ["/var/lib/pydio/personal"]
#EXPOSE 443
#CMD ["supervisord", "-n"]
#CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
#CMD ["/etc/init.d/pydiod"]
