FROM python:3.8
LABEL maintainer='Trae Horton<sorsnce@protonmail.com>'
RUN pip install requests
RUN pip install python-nmap
RUN mkdir /opt/Open-SOAR
RUN mkdir /opt/Open-SOAR/playbooks
RUN mkdir /opt/Open-SOAR/modules
ENV PYTHONPATH=/opt/Open-SOAR/modules
COPY modules/* /opt/Open-SOAR/modules/
COPY ssh_config /etc/ssh/ssh_config
# Make sure you put a valid Git repo to pull in Playbooks from SourceControl
ENV LOCATION "https://github.com/Sorsnce/Open-SOAR-public-playbooks.git"
RUN apt-get update
RUN apt-get -y install cron
RUN apt-get -y install openvpn
RUN apt-get -y install nmap
#ENTRYPOINT ls /opt/Open-SOAR/playbooks/
COPY ["bash_functions.sh","/bash_functions.sh"]
RUN chmod +x /bash_functions.sh

#CMD /usr/sbin/cron -f
ENTRYPOINT ["/bash_functions.sh"]
