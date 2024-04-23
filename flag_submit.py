import requests
from attack_script import attack
from data_process import Config


config = Config

def submit(array: tuple):  # 这个函数用来单进程提交flag
    flag = array[0]
    api = array[1].replace('[', '{').replace(']', '}')
    token = array[2]
    url = api.format(token=token, flag=flag)
    res = requests.get(url)
    print(res.text)


def attack_and_submit(ip: str):  # 这个函数用于攻击然后根据获取到的flag进行提交
    try:
        flag = attack(ip)
        print('\033[92m' + flag + '\033[0m')
        submit((flag, config.api, config.token))
    except:
        print('\033[31mIP:\033[0m', ip, '\033[31mattack failed!\033[0m')