def mealie_app(username=None, password=None, action=None, server=None, port=None, **kwargs):
    """
    This app allows you get interact with a Mealie cookbook server.

    Args:
        username (CEF type: username): This will be the username you use to log into the Mealie Server.
        password (CEF type: password): This will be the password you use to log into the Mealie Server.
        action: This should be what "action" you want to perform on the Mealie Server.
        server (CEF type: ip): This should be the DNS/IP address of the server.
        port (CEF type: port): This should be the port used to connect to the Mealie server.

    Returns a JSON-serializable object that implements the configured data paths:

    """

    import json
    # Uncomment this if you want to use this code in Splunk>Phantom custom function
    # import phantom.rules as phantom
    import requests

    def shoppinglist(username=None, password=None, server=None, port=None, **kwargs):
        headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        url = "http://{0}:{1}/api/auth/token".format(server, port)
        payload = "grant_type=&username={0}&password={1}&scope=&client_id=&client_secret=".format(username, password)
        r = requests.post(url, verify=False, json=payload, headers=headers)
        data = json.loads(r.text)
        token = data["access_token"]

        url2 = "http://{0}:{1}/api/meal-plans/1/shopping-list".format(server, port)
        headers2 = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded',
                    "Authorization": "Bearer {0}".format(token)}
        r2 = requests.get(url2, verify=False, headers=headers2)
        return r2.text

    if action == "shopping":
        data = shoppinglist(username=username, password=password, server=server, port=port)
        return data

    outputs = {}

    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
