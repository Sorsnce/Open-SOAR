FROM python:3.8
RUN mkdir /opt/Open-SOAR
RUN mkdir /opt/Open-SOAR/playbooks
RUN git clone https://sorsnce:3b5827d684920685bfbd17d0c1dc5c379dc4acb1@github.com/Sorsnce/soar.git
RUN mv soar /opt/Open-SOAR/playbooks
