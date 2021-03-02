FROM python:3.8-slim-buster
LABEL maintainer='Trae Horton<sorsnce@protonmail.com>'
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /opt/Open-SOAR
RUN mkdir /opt/Open-SOAR/playbooks
RUN mkdir /opt/Open-SOAR/modules
ENV PYTHONPATH=/opt/Open-SOAR/modules
COPY modules/* /opt/Open-SOAR/modules/

COPY install-packages.sh .
# Make sure you put a valid Git repo to pull in Playbooks from SourceControl
ENV LOCATION "https://github.com/Sorsnce/Open-SOAR-public-playbooks.git"

COPY ["bash_functions.sh","/bash_functions.sh"]
RUN chmod +x /bash_functions.sh
RUN chmod +x /install-packages.sh
RUN ./install-packages.sh
COPY ssh_config /etc/ssh/ssh_config

#CMD /usr/sbin/cron -f
ENTRYPOINT ["/bash_functions.sh"]
