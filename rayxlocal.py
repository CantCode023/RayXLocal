# Main Handler (CODE BRAIN)

import socket
import os
import time
import validators
import requests
from urllib.request import urlopen, Request
import hashlib


def Input(name):
    a = str(input(name))
    return a


def HOME():
    print("""
RayX LOCAL  
1. Get IP
2. Get Hostname
3. Check URL
4. Home
5. Quit
6. testing auto update
    """)


def IP():
    print(socket.gethostbyname(socket.gethostname()))


def HOSTNAME():
    print(socket.gethostname())


def CHECK_URL(LINK):
    a = validators.url(LINK)
    if a:
        print("VALID URL!")
    else:
        print("URL IS NOT VALID!")


def RELOAD():
    CLEAR()
    exec(requests.get(
        "https://raw.githubusercontent.com/CantCode023/RayXLocal/master/rayxlocal.py").text)
    quit()


def CLEAR():
    os.system("clear")


def QUIT():
    CLEAR()
    quit()


def CHECK_UPDATE():
    url = urlopen(Request("https://raw.githubusercontent.com/CantCode023/RayXLocal/master/rayxlocal.py", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})).read()
    currentupdate = hashlib.sha224(url).hexdigest()
    try:
        url = urlopen(Request("https://raw.githubusercontent.com/CantCode023/RayXLocal/master/rayxlocal.py", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})).read()
        currentupdate = hashlib.sha224(url).hexdigest()
        time.sleep(1)
        url = urlopen(Request("https://raw.githubusercontent.com/CantCode023/RayXLocal/master/rayxlocal.py", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})).read()
        newhash = hashlib.sha224(url).hexdigest()
        if newhash == currentupdate:
            pass
        else:
            print("NEW VERSION IS FOUND! AUTO UPDATING!")
            time.sleep(2)
            RELOAD()
    except Exception as e:
        print("There was an error when auto updating!\n{}".format(e))


def IFHANDLER(a):
    if a == "1":
        IP()
        time.sleep(2)
    elif a == "2":
        HOSTNAME()
        time.sleep(2)
    elif a == "3":
        print("1. BACK\n2. QUIT")
        a = Input("URL: ")
        if a == "1":
            CLEAR()
        elif a == "2":
            QUIT()
        else:
            CHECK_URL(a)
            time.sleep(2)
    elif a == "4":
        CLEAR()
    elif a == "5":
        QUIT()
    else:
        print("Wrong number! Choose again!")
        time.sleep(2)
        CLEAR()


def MAIN():
    while True:
        CHECK_UPDATE()
        HOME()
        a = Input("[:] ")
        IFHANDLER(a)


MAIN()