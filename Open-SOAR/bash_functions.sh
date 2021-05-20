#!/bin/bash

git clone $LOCATION /opt/Open-SOAR/playbooks
ls /opt/Open-SOAR/playbooks
chmod +x /opt/Open-SOAR/playbooks/*
mv /opt/Open-SOAR/playbooks/running-playbooks /etc/cron.d/
crontab -u root /etc/cron.d/running-playbooks
/usr/sbin/cron -f
