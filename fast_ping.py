# #
# from os import system

# url = '192.168.44.X'
# alive_ips = []
# for i in range(256):
#     ip = url.replace('X', str(i))
#     # print(ip)
#     result = system('ping {} -n 1'.format(ip))
#     print(result)
#     if result == 0:
#         alive_ips.append(ip)
# print(alive_ips)

# ['192.168.44.0', '192.168.44.5', '192.168.44.6', '192.168.44.8', '192.168.44.9', '192.168.44.11', '192.168.44.12', '192.168.44.13', '192.168.44.15', '192.168.44.17', '192.168.44.18', '192.168.44.19', '192.168.44.20', '192.168.44.21', '192.168.44.22', '192.168.44.23', '192.168.44.24', '192.168.44.25', '192.168.44.26', '192.168.44.27', '192.168.44.28', '192.168.44.29', '192.168.44.30', '192.168.44.31', '192.168.44.33', '192.168.44.35', '192.168.44.36', '192.168.44.39', '192.168.44.47', '192.168.44.48', '192.168.44.50', '192.168.44.51', '192.168.44.52', '192.168.44.53', '192.168.44.56', '192.168.44.57', '192.168.44.59', '192.168.44.60', '192.168.44.61', '192.168.44.62', '192.168.44.63', '192.168.44.65', '192.168.44.67', '192.168.44.68', '192.168.44.71', '192.168.44.72', '192.168.44.73', '192.168.44.74', '192.168.44.75', '192.168.44.76', '192.168.44.77', '192.168.44.78', '192.168.44.80', '192.168.44.81', '192.168.44.83', '192.168.44.84', '192.168.44.86', '192.168.44.87', '192.168.44.88', '192.168.44.89', '192.168.44.90', '192.168.44.91', '192.168.44.94', '192.168.44.95', '192.168.44.98', '192.168.44.99', '192.168.44.101', '192.168.44.103', '192.168.44.104', '192.168.44.105', '192.168.44.106', '192.168.44.108', '192.168.44.110', '192.168.44.113', '192.168.44.114', '192.168.44.115', '192.168.44.116', '192.168.44.117', '192.168.44.118', '192.168.44.120', '192.168.44.122', '192.168.44.124', '192.168.44.125', '192.168.44.126', '192.168.44.127', '192.168.44.128', '192.168.44.129', '192.168.44.130', '192.168.44.131', '192.168.44.133', '192.168.44.134', '192.168.44.135', '192.168.44.136', '192.168.44.137', '192.168.44.138', '192.168.44.140', '192.168.44.143', '192.168.44.149', '192.168.44.151', '192.168.44.155', '192.168.44.159', '192.168.44.161', '192.168.44.163', '192.168.44.165', '192.168.44.166', '192.168.44.167', '192.168.44.168', '192.168.44.169', '192.168.44.170', '192.168.44.171', '192.168.44.172', '192.168.44.173', '192.168.44.174', '192.168.44.175', '192.168.44.178', '192.168.44.179', '192.168.44.180', '192.168.44.182', '192.168.44.183', '192.168.44.184', '192.168.44.186', '192.168.44.187', '192.168.44.188', '192.168.44.189', '192.168.44.190', '192.168.44.191', '192.168.44.192', '192.168.44.193', '192.168.44.197', '192.168.44.200', '192.168.44.202', '192.168.44.203', '192.168.44.204', '192.168.44.209', '192.168.44.210', '192.168.44.212', '192.168.44.214', '192.168.44.216', '192.168.44.217', '192.168.44.218', '192.168.44.220', '192.168.44.221', '192.168.44.224', '192.168.44.225', '192.168.44.226', '192.168.44.227', '192.168.44.229', '192.168.44.230', '192.168.44.231', '192.168.44.233', '192.168.44.234', '192.168.44.235', '192.168.44.238', '192.168.44.239', '192.168.44.245', '192.168.44.247', '192.168.44.248', '192.168.44.249', '192.168.44.253', '192.168.44.254']
# 上边的代码是一个单线程的ping扫描，如果一直报错则使用上面的代码，虽然慢，但是稳定
##############################################################################################################
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

    with Pool(processes=16) as pool:  # 根据需要设置进程数
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
    print(alive_ips)
    with open('info/alive_ips.txt', 'w') as f:
        for i in alive_ips:
            f.write(i)
            f.write('\n')

# 上面是一个多线程 ping 扫描，更推荐用下面的 fscan ，但是仅限于真正的ip地址 
##############################################################################################################

# import subprocess

# def convert_to_cidr(ip_address):
#     """
#     将一个形如 219.217.199.X 的IP地址转换为网段形式 219.217.199.0/24
#     :param ip_address: 输入的IP地址，例如 "219.217.199.X"
#     :return: 转换后的网段，例如 "219.217.199.0/24"
#     """

#     # 分割IP地址
#     parts = ip_address.split('.')
#     if len(parts) != 4:
#         raise ValueError("Invalid IP address format")
    
#     # 提取前三段并构造网段
#     network_prefix = '.'.join(parts[:3]) + '.0'
#     cidr_notation = f"{network_prefix}/24"
#     return cidr_notation

    
# def fscan_ip(ip):

#     result = subprocess.run(
#             ['fscan.exe', "-h", ip ,'-nopoc', '-noredis', '-nobr', '-m', 'icmp'],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#         )
#     return result

# def main_function_to_execute(url):
#     result = fscan_ip(url)
#     alive_ips = []
#     for line in result.stdout.splitlines():
#         # print(line)
#         if b'Target' in line:
#             alive_ips.append(line.split()[2].decode())
#     # print(alive_ips)
#     with open('info/alive_ips.txt', 'w') as f:
#         for i in alive_ips:
#             f.write(i)
#             f.write('\n')
#     print('\033[34mScan finish, this is alive ips:\033[0m', *alive_ips, sep='\n')

# if __name__ == '__main__':

#     main_function_to_execute('219.217.199.0/24')

