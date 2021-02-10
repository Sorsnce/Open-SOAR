import nmap
import json


def scan(ip=None, **kwargs):
    nm = nmap.PortScanner()
    data = nm.scan(ip, arguments='-Pn -sV -sC --script http-enum')
    rawdata = data["scan"][ip]["tcp"]
    try:
        if 80 in rawdata:
            http_enum = rawdata['80']['script']['http-enum']
        elif 443 in rawdata:
            http_enum = rawdata['443']['script']['http-enum']
        else:
            http_enum = "http-enum didn't run"

        data = json.dumps(rawdata, indent=3)
        jsondata = json.dumps(http_enum, indent=3)
    except:
        data = "http-enum didn't run properly"
        jsondata = data
    outputs = {
        'nmap_output': data,
        'http_enum': jsondata
    }
    return outputs
