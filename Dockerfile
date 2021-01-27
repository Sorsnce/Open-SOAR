FROM python:3.8
RUN mkdir /opt/Open-SOAR
RUN mkdir /opt/Open-SOAR/playbooks
RUN mkdir /opt/Open-SOAR/modules
ARG PYTHONPATH=/opt/Open-SOAR/modules
COPY food_selector.py /opt/Open-SOAR/modules/
COPY smtp.py /opt/Open-SOAR/modules/
# Make sure you put a valid Git repo to pull in Playbooks from SourceControl
RUN git clone https://sorsnce:3b5827d684920685bfbd17d0c1dc5c379dc4acb1@github.com/Sorsnce/soar-playbooks.git
RUN mv /soar-playbooks/* /opt/Open-SOAR/playbooks
RUN apt-get update
RUN apt-get -y install cron
RUN mv /opt/Open-SOAR/playbooks/running-playbooks /var/spool/cron/crontabs/
