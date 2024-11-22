

import requests
import random
import requests
import json
import pyfiglet
import sys
import time
import os
import uuid
import webbrowser
import fake_useragent
os.system("pip install pyfiglet")
os.system("pip install fake_useragent")
os.system("clear")


Ab = '\033[1;92m'
aB = '\033[1;91m'
AB = '\033[1;96m'
aBbs = '\033[1;93m'
AbBs = '\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("SafeUm")
print(a_bSa + ab)


def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)


to(
    f"\033[31;m Script Type>> \033[1;36mSafeUm Account Maker \n\033[1;31m Telegram >>\033[1;33m@Abdullha_404\n\033[31;m Creator >>\033[1;33m@R3P1TA\n\033[31;m Tool Status >>\033[1;33mWorking\n\033[31;m Tool Value >>\033[1;33mFree Script\n\033[31;m Time >>\033[1;33m24 Hours\n\033[31;m")
print('')
print('\033[32;m')

from os import system, name
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

try:
    from websocket import create_connection
except:
    system('pip install websocket-client')
    from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []


def work():
    global failed, success, retry
    username = choice('qwertyuioplkjhgfdsazxcvbnm') + ''.join(choices(list('qwertyuioplkjhgfdsazxcvbnm1234567890'), k=13))
    try:
        con = create_connection("wss://195.13.182.217/Auth",
                                header={"app": "com.safeum.android", "host": None, "remoteIp": "195.13.182.217",
                                        "remotePort": str(8080), "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
                                        "time": "2023-04-30 12:13:32", "url": "wss://51.79.208.190/Auth"},
                                sslopt={"cert_reqs": CERT_NONE})
        con.send(dumps(
            {"action":"Register","subaction":"Desktop","locale":"en_IN","gmt":"+05","password":{"m1x":"1a07f431a68b4fb69a5c96349137476cca613f019b1016e63a27e022ef09805c","m1y":"ba83a1300f777ada673afb9bc4d507da3000ea2fabaaa35a6616a0af666a4bb7","m2":"43c58959c91b494e05a47cad7bca5b5f52e5204d393e06829c34884fa807954b","iv":"140c409aba2f6c7050518a826e6f2810","message":"5080dc99f8e226891ee1f4b52a480e1d0278ff1c211e5107a5de2ceb6a646d407084bd88f05438f6f671e2574239abbe68b401980a9336947e0b47c5e56bbcf05ad345cd46958d090bdd9110fdd33b08"},"magicword":{"m1x":"e90328d307cc09e8efb4bc307b93711c30ddc8dd2c81a4375a8c6f56cc491b6c","m1y":"c10d0ea9f845ede4e3bddabd688b5a5df39e0542a9f7e3d3e634a0c947eb7cef","m2":"0743248643a4ce7fe349e117aadc8bf6b98361410d9ee87b4a8b7519ddf421d5","iv":"186e765c4b10803fc9a6a9d6ae08549b","message":"76f4c2466364ccf3bd38882471fc30c3"},"magicwordhint":"0000","login":str(username),"devicename":"Xiaomi 220733SPH","softwareversion":"1.1.0.1548","nickname":"jsjkkm822mmsm","os":"AND","deviceuid":"3933b21c103ad7a8","devicepushuid":"*fC4qytGbRgCLyGKiZRfh5n:APA91bFXieRxcxPxIyxknU-MNLUyrao13YgiKV_tthXzXVLToRz8-t6LkU2Zol8cW7jhcfQp10h0n0VyZw4vOY04HWS5fIXGX-ic_1ijzt3RGbKUBCEkqAg","osversion":"and_12.0.0","id":"1492923070"}))
        gzip = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in gzip:
            success += 1
            b = accounts.append(username + ':mmmm')
            print(b)
            with open('tanji-Accounts.txt', 'a') as f:
                f.write(username + ":mmmm | TG : @Abdullha_404\n")

        else:
            failed += 1
    except:
        retry += 1


start = ThreadPoolExecutor(max_workers=1000)

while True:
    start.submit(work)
    print('\n\n\n' + ' ' * 25 + 'Success : ' + str(success) + '\n\n\n' + ' ' * 25 + 'Failed : ' + str(
        failed) + '\n\n\n' + ' ' * 25 + 'ReTry : ' + str(retry))
    hh = str(failed) + str(success) + str(retry)
    if int(success) >= 50:
        fuck()
        print("Created Accounts Successfully Sent To Owner Group")

    if int(success) > int(0):
        z = "\n".join(accounts)
        
        print("Account Generated>>\n", z)
        

    os.system('clear')
    