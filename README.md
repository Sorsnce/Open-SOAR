# Open-SOAR
Open-SOAR is a project to allow opensource containerized workflows to allow Security Orchestration Automation and Response. 

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
