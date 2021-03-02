def nessus_app(server=None, username=None, password=None, cve_list=None, scan_id=None, action=None, **kwargs):
    """
    This custom function will perform several actions within Nessus Professional and Nessus Home edition.

    Args:
        server (CEF type: ip): This will be the IP address or DNS address of the Nessus scanner we are wanting to
        interact with.
        username (CEF type: username): This will be the username you use to log into the Nessus scanner.
        password (CEF type: password): This will be the password you use to log into the Nessus scanner. This cannot be
        an API key due to the limitations of Nessus Home edition.
        cve_list (CEF type: CVE): This will be a list of CVEs you want to lookup in a specific scan within the Nessus
        Scanner. The format should be : ["CVE-2018-12076","CVE-2020-1245","CVE-2021-5432"]
        scan_id: This should be the scan ID in the Nessus Scaner. You can find the scan ID by looking at the URL in the
        nessus scanner. Example, open the results of your scan in the Nessus Scanner. Look at the URI,
        http://nussusscaner:8834/#/scans/reports/90/hosts - 90 would be your scan ID
        action: This should be what "action" you want to perform on the Nessus Scanner. Such as cve, scan, etc.

    Returns a JSON-serializable object that implements the configured data paths:

    """

    import requests
    import json
    # Uncomment this if you want to use this code in Splunk>Phantom custom function
    #import phantom.rules as phantom

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
            url2 = "https://{0}:8834/scans/{2}?filter.0.quality=eq&filter.0.filter=cve&filter.0.value={1}".format(
                server, item, scan_id)
            header = {'X-API-Token': apitoken, 'X-Cookie': 'token=' + token}
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
                outputs = "No CVE found in Nessus"
        return outputs

    def nessus_scan(server=None, username=None, password=None, scan_id=None, **kwargs):
        """
        test scan for nessus

        Returns a JSON-serializable object that implements the configured data paths:

        """

        url3 = "https://{0}:8834/nessus6.js".format(server)
        a = requests.get(url3, verify=False)
        apitoken = a.text.split('key:"getApiToken",value:function(){')[1].split('}')[0].split('return"')[1][:-1]
        headers = {'X-API-Token': apitoken}
        url = "https://{0}:8834/session".format(server)
        payload = {"username": username, "password": password}
        r = requests.post(url, headers=headers, verify=False, json=payload)
        data = json.loads(r.text)
        token = data["token"]
        url2 = "https://{0}:8834/scans/{1}/launch".format(server, scan_id)
        header = {'X-API-Token': apitoken, 'X-Cookie': 'token=' + token}
        r = requests.post(url2, headers=header, verify=False)
        message = "Scan {0} successfully started".format(scan_id)
        return message

    if action == "cve":
        data = cve_lookup(server=server, username=username, password=password, cve_list=cve_list, scan_id=scan_id)
    elif action == "scan":
        data = nessus_scan(server=server, username=username, password=password, scan_id=scan_id)

    outputs = {"data": data}

    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
