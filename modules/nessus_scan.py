def nessus_scan(server=None, username=None, password=None, scan_id=None, **kwargs):
    """
    test scan for nessus

    Returns a JSON-serializable object that implements the configured data paths:

    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import requests

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
