from netmiko import ConnectHandler


def cisco_asa(device=None, username=None, password=None, port=None, secret=None, action=None, **kwargs):
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



