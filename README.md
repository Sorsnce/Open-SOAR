# Open-SOAR
Open-SOAR is a project to allow opensource containerized workflows to allow Security Orchestration Automation and Response. 

---

[![Docker Pulls](https://img.shields.io/docker/pulls/sorsnce/open-soar.svg)](https://hub.docker.com/r/sorsnce/open-soar)
[![Dependency Status](https://shields.io/librariesio/release/github/sorsnce/Open-SOAR)](https://github.com/Sorsnce/Open-SOAR/network/dependencies)
[![GitHub Release](https://img.shields.io/github/release/sorsnce/Open-SOAR.svg)](https://github.com/sorsnce/Open-SOAR/releases/latest)


---

```
$ git clone https://github.com/Sorsnce/Open-SOAR.git
$ cd Open-SOAR.git
$ docker build .
$ docker run -ti <docker image>
```
To help debug any issues you can drop into the shell of the container by using the following code:
```
$ docker run -ti <docker image> /bin/bash
```
