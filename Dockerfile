FROM python:3.8
LABEL maintainer='Trae Horton<sorsnce@protonmail.com>'
RUN pip install requests
RUN mkdir /opt/Open-SOAR
RUN mkdir /opt/Open-SOAR/playbooks
RUN mkdir /opt/Open-SOAR/modules
ENV PYTHONPATH=/opt/Open-SOAR/modules
COPY modules/* /opt/Open-SOAR/modules/
# Make sure you put a valid Git repo to pull in Playbooks from SourceControl
#ARG github_repo
#RUN git clone github_repo
#RUN mv /soar-playbooks/* /opt/Open-SOAR/playbooks
#RUN chmod +x /opt/Open-SOAR/playbooks/*
RUN apt-get update
RUN apt-get -y install cron
#RUN mv /opt/Open-SOAR/playbooks/running-playbooks /etc/cron.d/
#RUN crontab -u root /etc/cron.d/running-playbooks
#CMD git clone github_repo
CMD ["-repo"]
CMD mv /soar-playbooks/* /opt/Open-SOAR/playbooks
CMD chmod +x /opt/Open-SOAR/playbooks/*
CMD mv /opt/Open-SOAR/playbooks/running-playbooks /etc/cron.d/
CMD crontab -u root /etc/cron.d/running-playbooks
CMD cat /etc/cron.d/running-playbooks
CMD /usr/sbin/cron -f
