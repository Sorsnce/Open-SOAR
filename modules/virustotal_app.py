import json
import requests


def hash_lookup(fileHash=None, apikey=None, **kwargs):
    print("VirusTotal Hash lookup for: " + fileHash)
    apierror = False
    # VT Hash Checker
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': apikey, 'resource': fileHash}
    response = requests.get(url, params=params)

    try:  # EAFP
        result = response.json()
    except:
        apierror = True
        print("Error: Invalid API Key")

    if not apierror:
        if result['response_code'] == 0:
            print("Hash was not found in Malware Database")
        elif result['response_code'] == 1:
            report = str(result['positives']) + "/" + str(result['total'])
            link = "https://www.virustotal.com/gui/file/" + fileHash + "/detection"
            outputs = {"File Hash": fileHash,
                       "First Seen on VirusTotal": str(result['scan_date']),
                       "VirusTotal Report": report,
                       "Report Link": link
                       }
            assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
            return outputs
        else:
            print("No Reponse")


