def tenable_sc_app(server=None, username=None, password=None, action=None, data1=None, data2=None, **kwargs):
    """
    This app allows you to interact with Tenable.SC. The app allows actions such as asset list updates etc.
    
    Args:
        server (CEF type: ip): This should be the ip or dns address of the Tenable.SC
        username: This should be the username you would use to log into Tenable.SC
        password: This should be the password you would use to log into Tenable.SC
        action: This will be the action you make to take within Tenable.SC
        data1: This will be variable data passed to the function based on the action
        data2: This will be variable data passed to the function based on the action
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """

    import json
    import re
    from tenable.sc import TenableSC
    # Uncomment this if you want to use this code in Splunk>Phantom custom function
    #import phantom.rules as phantom

    sc = TenableSC(server)
    sc.login(username, password)

    def assetlist_update(assetid=None, newassetid=None):
        sc = TenableSC(server)
        sc.login(username, password)
        assetlist = sc.asset_lists.details(assetid, fields=["viewableIPs"])["viewableIPs"][1]['ipList']
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', assetlist)
        sc.asset_lists.edit(newassetid, ips=ip)

    if action == "assetlist":
        assetlist_update(assetid=data1, newassetid=data2)

    outputs = {}
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs

