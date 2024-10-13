#
# from os import system
#
# url = '192-168-1-X.pvp4188.bugku.cn'
# alive_ips = []
# for i in range(256):
#     ip = url.replace('X', str(i))
#     # print(ip)
#     result = system('ping {} -n 2'.format(ip))
#     print(result)
#     if result == 0:
#         alive_ips.append(ip)
# print(alive_ips)

# 上边的代码是一个单线程的ping扫描，如果一直报错则使用上面的代码，虽然慢，但是稳定
from multiprocessing import Pool
from os import system


def check_ip(ip):
    result = system('ping -n 1 {} >NUL'.format(ip))
    if result == 0:
        return ip
    return None


def check_ip_signal(ip):
    result = system('ping {} -n 1'.format(ip))
    if result == 0:
        return ip
    return None


def main_function_to_execute(url):
    print('\033[34m Scaning ... \033[0m')
    ips_to_check = [url.replace('X', str(i)) for i in range(256)]

    with Pool(processes=32) as pool:  # 根据需要设置进程数
        alive_ips = pool.map(check_ip, ips_to_check)

    alive_ips = [ip for ip in alive_ips if ip is not None]
    with open('info/alive_ips.txt', 'w') as f:
        for i in alive_ips:
            f.write(i)
            f.write('\n')
    print('\033[34mScan finish, this is alive ips:\033[0m', *alive_ips, sep='\n')


if __name__ == '__main__':
    url = input('input url:')
    # url = '219.217.199.X'
    ips_to_check = [url.replace('X', str(i)) for i in range(256)]

    with Pool(processes=32) as pool:  # 根据需要设置进程数
        alive_ips = pool.map(check_ip_signal, ips_to_check)

    alive_ips = [ip for ip in alive_ips if ip is not None]
    with open('info/alive_ips.txt', 'w') as f:
        for i in alive_ips:
            f.write(i)
            f.write('\n')
    print(alive_ips)
