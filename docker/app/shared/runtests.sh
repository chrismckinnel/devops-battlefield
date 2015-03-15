#! /bin/bash

trap "[[ -f /var/www/makefile ]] && rm /var/www/makefile" EXIT

ln -sf /tmp/makefile /var/www/makefile

export DJANGO_SETTINGS_MODULE=conf.docker
make link_not_found_image
/var/www/runtests.sh
