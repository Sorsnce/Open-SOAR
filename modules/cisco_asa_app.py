def cisco_asa(device=None, username=None, password=None, port=None, secret=None, action=None, ip_address=None, **kwargs):
    """
    Args:
        device (CEF type: ip): This should be the ip or dns address of the cisco asa
        username (CEF type: username): This should be the username you would use to SSH into the cisco asa
        password (CEF type: password): This should be the password you would use to SSH into the cisco asa
        port (CEF type: port): This would be the port you would use to SSH into the cisco asa. Default is TCP/22
        secret (CEF type: password): This is the `enable` password within a cisco asa
        action: This will be the "action" you are wanting to take on the cisco asa. You can see in the if statement what your options are.
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    from netmiko import ConnectHandler
    import json
    # Uncomment this if you want to use this code in Splunk>Phantom custom function
    #import phantom.rules as phantom
    asa = {
        'device_type': 'cisco_asa',
        'host':   device,
        'username': username,
        'password': password,
        'port' : port,          # optional, defaults to 22
        'secret': secret,     # optional, defaults to ''
    }

    if action == "shut":
        commands = ['conf t', 'int g1/3', 'shut']
        net_connect = ConnectHandler(**asa)
        net_connect.find_prompt()
        net_connect.send_config_set(commands)
        print("blocked port")
    elif action == "no shut":
        commands = ['conf t', 'int g1/3', 'no shut']
        net_connect = ConnectHandler(**asa)
        net_connect.find_prompt()
        net_connect.send_config_set(commands)
        print("unblocked port")
    elif action == "block ip":
        for ip in ip_address:
            commands = ['conf t', 'object-group network BLACKLIST', 'network-object {0} 255.255.255.255'.format(ip)]
            net_connect = ConnectHandler(**asa)
            net_connect.find_prompt()
            net_connect.send_config_set(commands)
        print("IP address added to BLACKLIST")


    outputs = {}
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs