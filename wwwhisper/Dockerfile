FROM centos:centos7

MAINTAINER Lars Solberg <lars.solberg@gmail.com>
ENV REFRESHED_AT 2014-08-10
ENV NGINX_VERSION 1.4.4

RUN yum localinstall -y http://dl.fedoraproject.org/pub/epel/beta/7/x86_64/epel-release-7-0.2.noarch.rpm
RUN yum install -y tar git make gcc pcre-devel openssl-devel python-setuptools python-devel wget && \
    easy_install pip && \
    pip install supervisor virtualenv

# Install nginx and the required module (needs to be compiled in....)
RUN wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \
    tar -zxvf nginx-${NGINX_VERSION}.tar.gz && \
    cd nginx-${NGINX_VERSION} && \
    git clone https://github.com/PiotrSikora/ngx_http_auth_request_module.git && \
    ./configure --add-module=./ngx_http_auth_request_module/ --with-http_ssl_module --with-http_sub_module --user=www-data --group=www-data --prefix=/usr/local/nginx/ --sbin-path=/usr/local/sbin && \
    make && make install

RUN wget https://github.com/jwilder/docker-gen/releases/download/0.3.2/docker-gen-linux-amd64-0.3.2.tar.gz && \
    tar xvzf docker-gen-linux-amd64-0.3.2.tar.gz

RUN adduser --system www-data && adduser --system -G www-data wwwhisper
RUN cd / && git clone https://github.com/wrr/wwwhisper.git && cd wwwhisper && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt

ADD sites.tmpl /
ADD index.tmpl /
ADD supervisord.conf /
ADD docker-gen.conf /
ADD nginx.conf /usr/local/nginx/conf/nginx.conf

ADD start /start
RUN chmod 755 /start
ENTRYPOINT ["/bin/bash", "-e", "/start"]
CMD ["start"]

ENV DOCKER_HOST unix:///docker.sock
EXPOSE 80
