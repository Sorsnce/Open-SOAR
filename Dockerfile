FROM python:3.8
LABEL maintainer='Trae Horton<sorsnce@protonmail.com>'
RUN pip install requests
RUN mkdir /opt/Open-SOAR
RUN mkdir /opt/Open-SOAR/playbooks
RUN mkdir /opt/Open-SOAR/modules
ENV PYTHONPATH=/opt/Open-SOAR/modules
COPY modules/* /opt/Open-SOAR/modules/
# Make sure you put a valid Git repo to pull in Playbooks from SourceControl
ENV LOCATION "git clone https://github.com/Sorsnce/Open-SOAR-public-playbooks.git"
RUN apt-get update
RUN apt-get -y install cron
#ENTRYPOINT ls /opt/Open-SOAR/playbooks/
COPY ["bash_functions.sh","/bash_functions.sh"]
RUN chmod +x /bash_functions.sh

#CMD /usr/sbin/cron -f
ENTRYPOINT ["/bash_functions.sh"]
