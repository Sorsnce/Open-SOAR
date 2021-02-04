import requests
import json


def cve_lookup(server=None, username=None, password=None, cve_list=None, scan_id=None, **kwargs):
    outputs = {}
    cve = cve_list
    print(cve)
    url3 = "https://{0}:8834/nessus6.js".format(server)
    a = requests.get(url3, verify=False)
    apitoken = a.text.split('key:"getApiToken",value:function(){')[1].split('}')[0].split('return"')[1][:-1]
    headers = {'X-API-Token': apitoken}
    url = "https://{0}:8834/session".format(server)
    payload = {"username": username, "password": password}
    r = requests.post(url, headers=headers, verify=False, json=payload)
    data = json.loads(r.text)
    token = data["token"]
    for item in cve:
        url2 = "https://{0}:8834/scans/{2}?filter.0.quality=eq&filter.0.filter=cve&filter.0.value={1}".format(server, item, scan_id)
        header = {'X-API-Token': apitoken, 'X-Cookie': 'token='+token}
        r = requests.get(url2, headers=header, verify=False)
        data = json.loads(r.text)
        if len(data['hosts']) != 0:
            amount = len(data['hosts'])
            counter = 0
            list_ips = []
            while counter != amount:
                ips = data['hosts'][counter]['hostname']
                list_ips.append(ips)
                counter += 1
            outputs[item] = list_ips
        else:
            print("No CVE found in Nessus")
    return outputs


def nessus_scan(server=None, username=None, password=None, scan_id=None, **kwargs):
    """
    test scan for nessus

    Returns a JSON-serializable object that implements the configured data paths:

    """
    ############################ Custom Code Goes Below This Line #################################

    # Write your custom code here...
    url3 = "https://"+server+":8834/nessus6.js"
    a = requests.get(url3, verify=False)
    apitoken = a.text.split('key:"getApiToken",value:function(){')[1].split('}')[0].split('return"')[1][:-1]
    headers = {'X-API-Token': apitoken}
    url = "https://"+server+":8834/session"
    payload = {"username": username, "password": password}
    r = requests.post(url, headers=headers, verify=False, json=payload)
    data = json.loads(r.text)
    token = data["token"]
    url2 = "https://htb.sorsnce.com:8834/scans/"+scan_id+"/launch"
    header = {'X-API-Token': apitoken, 'X-Cookie': 'token=' + token}
    r = requests.post(url2, headers=header, verify=False)
    # Return a JSON-serializable object
    outputs = {}
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    message = "Scan {0} successfully started".format(scan_id)
    return message
