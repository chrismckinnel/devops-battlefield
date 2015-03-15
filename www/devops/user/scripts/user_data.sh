#! /bin/bash

PUBLIC_DNS=$(curl http://169.254.169.254/latest/meta-data/public-hostname)

sed -i s/PUBLIC_DNS/$PUBLIC_DNS/g /etc/nginx/sites-enabled/app
sed -i s/PUBLIC_DNS/$PUBLIC_DNS/g /var/www/conf/prod.py
