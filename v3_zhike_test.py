import json

import pickle
from time import sleep

import requests
import socket
import urllib.parse


def get_out_ip():
    localIP = socket.gethostbyname(socket.gethostname())  # 得到本地ip
    print("local ip:%s " % localIP)

    ipList = socket.gethostbyname_ex(socket.gethostname())
    for i in ipList:
        if i != localIP:
            print("external IP:%s" % i)

    url = 'http://ip.taobao.com/service/getIpInfo2.php'
    headers={
        'Host': 'ip.taobao.com',
        'Content - Length': '7',
        'Origin':'http://ip.taobao.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept':'*/*',
        'X-Requested-With':'XMLHttpRequest',
        'Referer':'http://ip.taobao.com/ipSearch.php',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,ja;q=0.6',
        'Cookie':'t=f7c0ab27cfbcefda5f877f9117af52b7; cookie2=12a4d43bb0f75002d8df93e8d466baaf; v=0; _tb_token_=e337e833e3a3d; PHPSESSID=1f1n2v4qs60ck7so7hcforja67',
        'Content-Type':'application/x-www-form-urlencoded',
    }
    r = requests.post(url,headers=headers,data='ip=myip')
    pspm_result = json.loads(r.content)
    ip = pspm_result['data']['ip']
    print('ip='+ip)
    # 获取外网IP
    return ip

headers = {'Host': 'api.pingstart.com',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
    }
#proxies = {"http": '162.243.38.127:80'}

def pmpm_result():
    pspm_url = 'http://pspm.pingstart.com/api/campaigns?token=c602ccac-58a2-4e01-a271-4128de2937e7&publisher_id=1437'
    s = requests.session()
    req = s.get(pspm_url,headers=headers)
    pspm_result = json.loads(req.content)
    print('111')
    return pspm_result

def v3_result():
    v3_url = 'http://api.pingstart.com/v3/api/nativeads?publisherid=5079&slotid=1002700&lang=zh&timestamp=1504691452243&platform=android&osv=4.4.2&dpi=640.0&tzone=GMT%2B08%3A00&aid=2ba2f9148cb67141&gaid=005653pl-7f2e-4512-b2f1-f528bccd4810&orientation=1&density=4.0&nt=1&model=LGLS990&brand=lge&gp=1&root=1&versioncode=3.5.1&app_versioncode=10004&app_name=com.pingstart.sample&ad_type=pic&num=5&from=onl'
    s = requests.session()
    req = requests.get(v3_url,headers=headers)
    v3_result_save = json.loads(req.content)['apps']
    print(v3_result_save)
    v3_result_save_click_url = json.loads(req.content)['apps'][0]['click_url']
    #print(v3_result_save_click_url)
    result = urllib.parse.urlparse(v3_result_save_click_url)
    sqcc = urllib.parse.parse_qs(result.query)
    campaign_id = sqcc['campaign_id'][0]
    print(campaign_id)
    with open('cam_id.txt', 'a+') as f:
        f.write(campaign_id+'\n')
    #fp.write(campaign_id)
    return  v3_result_save_click_url,campaign_id

if __name__ == '__main__':
    get_out_ip()
'''
    save_pspm_result = pmpm_result()
    qqq = str(save_pspm_result)
    i=0
    for i in range(100):
        if i < 100:
            i = i + 1
            try:
                save_v3_result = v3_result()
                sleep(3)
            except:
                sleep(3)
                pass
'''
    #print(save_v3_result[1])
    #print(qqq.find(save_v3_result[1]))


