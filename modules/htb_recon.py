import requests
import json
import time
import subprocess
import nmap


def htb_login(email=None, password=None, **kwargs):
    url = "https://www.hackthebox.eu/api/v4/login"
    header = {'Content-Type': 'application/json;charset=utf-8',
              'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    payload = {"email": email, "password": password}
    r = requests.post(url, json=payload, headers=header, verify=False)
    data = json.loads(r.text)
    token = data['message']['access_token']
    return token


def get_latest_box(token=None, **kwargs):
    url = "https://www.hackthebox.eu/api/v4/machine/list"
    headers = {'Content-Type': 'application/json;charset=utf-8',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
               'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    machine_id = data['info'][-1]['id']
    return machine_id


def box_details(machine_id=None, token=None, **kwargs):
    url = "https://www.hackthebox.eu/api/v4/machine/info/" + str(machine_id)
    headers = {'Content-Type': 'application/json;charset=utf-8',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
               'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    status = data['info']['isCompleted']
    box_status = data['info']['playInfo']['isActive']
    if (status == False):
        if (box_status == False):
            url2 = "https://www.hackthebox.eu/api/v4/machine/play/" + str(machine_id)
            r = requests.post(url2, headers=headers)
            time.sleep(45)
            r = requests.get(url, headers=headers)
            data = json.loads(r.text)
            ip = data['info']['ip']
            hostname = data['info']['name']
            avatar = data['info']['avatar']
            return ip, hostname, avatar
        elif (box_status == None):
            url2 = "https://www.hackthebox.eu/api/v4/machine/play/" + str(machine_id)
            r = requests.post(url2, headers=headers)
            time.sleep(45)
            r = requests.get(url, headers=headers)
            data = json.loads(r.text)
            ip = data['info']['ip']
            hostname = data['info']['name']
            avatar = data['info']['avatar']
            return ip, hostname, avatar
        else:
            r = requests.get(url, headers=headers)
            data = json.loads(r.text)
            ip = data['info']['ip']
            hostname = data['info']['name']
            avatar = data['info']['avatar']
            return ip, hostname, avatar
    else:
        testinfo = ""


def open_vpn(api_code=None, token=None, **kwargs):
    headers = {'Content-Type': 'application/json;charset=utf-8',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
               'Authorization': 'Bearer ' + token}
    url1 = "https://www.hackthebox.eu/api/labs/switch/usfree?api_token={0}".format(api_code)
    r = requests.post(url1, headers=headers)
    url = "https://www.hackthebox.eu/api/v4/access/ovpnfile"
    r = requests.get(url, headers=headers)
    cert = r.text
    f = open("htb.ovpn", "w")
    f.write(cert)
    f.close()
    path = 'htb.ovpn'
    x = subprocess.Popen(['sudo', 'openvpn', '--auth-nocache', '--config', path])
    time.sleep(15)
    return cert


def kill_ovpn():
    x = subprocess.Popen(['sudo', 'killall', 'openvpn'])
