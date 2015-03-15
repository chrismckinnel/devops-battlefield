FROM chrismckinnel/devops-battlefield-base:latest

WORKDIR /var/www

RUN easy_install -U pip
RUN cd /tmp && pip install -r requirements.txt && \
    pip install ipdb && \
    pip install django-template-debug==0.3.5


ADD docker/app/shared/start_webserver.sh /usr/local/bin/start_webserver.sh
ADD docker/app/shared/requirements.txt /tmp/requirements.txt
ADD docker/app/shared/make_install.sh /usr/local/bin/make_install.sh
ADD docker/app/shared/runtests.sh /usr/local/bin/runtests.sh
ADD docker/app/shared/makefile /tmp/makefile

CMD ["/usr/local/bin/start_webserver.sh"]

EXPOSE 8001
