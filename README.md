# Open-SOAR
Open-SOAR is a project to allow opensource containerized workflows to allow Security Orchestration Automation and Response. 

All Donations in Cryptocurrency are highly appreciated:

Bitcoin: 1QApAnZk7AhipRhVu367XeGDgxRriZ7zjv

Litecoin:MQ8MYBvBhJ4z8mAu1N9gjx33sXb9NuFyZg

Ethereum: 0x554489B7aE3B4Be4B4E82c473933725aeE29C417

---

[![Docker Pulls](https://img.shields.io/docker/pulls/sorsnce/open-soar.svg)](https://hub.docker.com/r/sorsnce/open-soar)
[![Dependency Status](https://img.shields.io/librariesio/release/github/sorsnce/open-soar)](https://github.com/Sorsnce/Open-SOAR/network/dependencies)
[![GitHub Release](https://img.shields.io/github/v/tag/sorsnce/open-soar)](https://github.com/sorsnce/Open-SOAR/releases/latest)


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
You can also run Open-SOAR on Synology NAS


# Splunk>Phantom
#### All functions listed in the `modules` directory are compatible with Splunk>Phantom
* Download the .py and .json for the custom function you want in Phnatom
* These can be found in the `modules` dirctory
* Run the following commands below
```
$ tar -cvzf phantom.tgz <.json file> <.py files>
```
###### EXAMPLE
```
$ tar -cvzf phantom.tgz cisco_asa_app.json cisco_asa_app.py
```

* Now upload the `phantom.tgz` file into **Splunk>Phantom** and you should now have the imported function.
