import fast_ping
import os
import time


class Init:  # 这个类用来初始化信息
    def __init__(self):
        if not os.path.exists('info'):  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs('info')
        else:
            print("---  info direction has exist  ---")
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
        with open("info/ssh_info.txt", "w") as f:
            f.write(input('Your host (such as: baidu.com):'))
            f.write('\n')
            f.write(input('Your username (such as: root)'))
            f.write('\n')
            f.write(input('Your password (such as: root)'))
            f.write('\n')
            f.write(input('Your port (such as: 22)'))
            f.write('\n')
        # print(url)
        fast_ping.main_function_to_execute(url)


class Config:  # 这个类用来读取信息
    def __init__(self):
        try:
            make_time = os.path.getmtime("info/ssh_info.txt")  # 修改时间
            if time.time() - make_time > 43200:  # 如果上个文件修改时间超过43200秒，则重新初始化
                print('\033[93mWarning: \033[0mThere has been a file but too old, start init')
                if input('Whether to re-init:(y/n)').lower() == 'y':
                    Init()
                else:
                    os.utime("info/token.txt", (time.time(), time.time()))
            else:
                print('\033[93mWarning: \033[0mThere has been a file named ssh_info.txt ')
        except FileNotFoundError:
            print('\033[93mFile not found\033[0m, start init')
            Init()  # 如果不存在这个文件，则初始化
        except:
            print('\033[31mSomething bad happened!!!!\033[0m')
            exit(0)

        self.api = self.read_api()
        self.attack_address = self.read_attack_address()
        self.token = self.read_token()
        if len(self.read_alive_ips()) <= 1:
            print('\033[31mWarning: \033[0mThere is only one ip alive, scaning again!')
            fast_ping.main_function_to_execute(self.attack_address)
        self.alive_ips = self.read_alive_ips()
        self.host, self.user, self.passwd, self.port = self.read_ssh_info()
        print('\n\033[31mConfirm you information: \033[0m\n', '\033[36mapi\033[0m:', self.api, '\n', '\033[36mtoken\033[0m:', self.token, '\n',
              '\033[36malive_ips\033[0m:', self.alive_ips, '\n',
              '\033[36mattack_address\033[0m:', self.attack_address, '\n')

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

    def read_ssh_info(self):
        with open('info/ssh_info.txt', 'r') as f:
            ssh_info = f.readlines()
        return ssh_info[0].strip(), ssh_info[1].strip(), ssh_info[2].strip(), ssh_info[3].strip()
