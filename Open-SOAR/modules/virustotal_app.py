def virustotal_app(filehash=None, apikey=None, **kwargs):
    """
    This app allows you to look up filehashes within VirusTotal. You need a valid VirusTotal API Key to use this app.
    
    Args:
        filehash (CEF type: hash): This should be a valid file hash such as MD5, SHA1, or SHA256
        apikey: This should be a valid VirusTotal API key. See the URI below to get APIKEY
            https://www.virustotal.com/gui/user/<username>/apikey
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    import json
    import requests
    # Uncomment this if you want to use this code in Splunk>Phantom custom function
    #import phantom.rules as phantom
    
    
    data = "VirusTotal Hash lookup for: {0}".format(filehash)
    apierror = False
    # VT Hash Checker
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': apikey, 'resource': filehash}
    response = requests.get(url, params=params)

    try:  # EAFP
        result = response.json()
    except:
        apierror = True
        data2 = "Error: Invalid API Key"

    if not apierror:
        if result['response_code'] == 0:
            data2 = "Hash was not found in Malware Database"
        elif result['response_code'] == 1:
            report = str(result['positives']) + "/" + str(result['total'])
            link = "https://www.virustotal.com/gui/file/{0}/detection".format(filehash)
            outputs = {"File Hash": filehash,
                       "First Seen on VirusTotal": str(result['scan_date']),
                       "VirusTotal Report": report,
                       "Report Link": link
                       }
            assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
            return outputs
        else:
            data2 = "No Reponse"

