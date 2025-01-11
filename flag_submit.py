import requests
from attack_script import attack
from data_process import Config


config = Config()

def submit(array: list):  # 这个函数用来单进程提交flag
    # print(array)
    flag = array[0].strip()
    api = array[1].replace('[', '{').replace(']', '}')
    token = array[2].strip()
    # print(api)
    url = api.format(token=token, flag=flag)
    print(url)
    res = requests.get(url)
    print(res.text.split('<h3 class="m-t-30">')[1].split('</h3>')[0])


def attack_and_submit(ip: str):  # 这个函数用于攻击然后根据获取到的flag进行提交
    try:
        config = Config()
        flag = attack(ip)
        print('\033[92m' + flag + '\033[0m')
        submit([flag, config.api, config.token])
    except:
        print('\033[31mIP:\033[0m', ip, '\033[31mattack failed!\033[0m')


if __name__ == '__main__':
    config = Config()
    attack_and_submit('192-168-1-208.pvp5670.bugku.cn')