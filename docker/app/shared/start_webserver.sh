#!/bin/bash

# /host is a volume mounted on the docker host
# Ensure we have correct directory structure
# to continue
set -e
[ -d /host/logs/supervisor ] || mkdir -p /host/logs/supervisor
[ -d /host/logs/uwsgi ] || mkdir -p /host/logs/uwsgi
[ -d /host/static ] || mkdir -p /host/static
[ -d /host/media ] || mkdir -p /host/media
[ -d /host/logs/emails ] || mkdir -p /host/logs/emails

chown -R www-data:www-data /host

#
# Helper functions
#
banner() {
    echo -e "===== $@ =====\n"
}

error() {
    echo -e "ERROR: $@\n\n"
    exit 1
}

for logfile in `ls /host/logs/*.log`; do
    banner "Docker (Re)Started" >> $logfile
    printf "[$(date)]\n\n" >> $logfile
done

DOCKER_CONFIG=/var/www/conf/docker.py
CONFIG_PATH=/var/www/conf/$ENV\.py
echo -e "===== Symlinking Configuration File =====\n\n\n"
ln -sf $CONFIG_PATH $DOCKER_CONFIG || error "Unable to symlink config file \n\nExiting....\n\n"

mkdir -p /var/run/uwsgi/                   && \
chown -R www-data:www-data /var/run/uwsgi/

/usr/local/bin/make_install.sh

cd /var/www
if [ "$ENV" == "local" ]; then
    rm -rf /etc/supervisor/conf.d/webserver.conf
    DJANGO_SETTINGS_MODULE=conf.docker ./manage.py runserver 0.0.0.0:$PORT &
fi

supervisord -n
