from multiprocessing import Pool
from flag_submit import submit, attack_and_submit
from data_process import Config
from file_download import *

if __name__ == '__main__':
    # 先是初始化信息部分
    config = Config()

    # 然后是下载文件部分
    if 'y'in input('是否打包web目录并下载pwn文件？(y/N)'):
        ssh = ssh_connect(config)
        ssh.pack_web()
        ssh.cp_pwn()
        ssh.close()
        sftp = sftp_connect(config)
        os.system('del *.tar.gz')
        print('缓存已清理')
        sftp.download()

    # 文件初始化结束，下面读取信息
    api = config.api
    token = config.token
    alive_ips = config.alive_ips

    with Pool(processes=16) as pool:  # 根据需要设置进程数!!!!!!!
        flag_list = pool.map(attack_and_submit, alive_ips)
    flag_list = [flag for flag in flag_list if flag is not None]

    # 之后对于所有的flag进行提交
    if flag_list and api and token:
        with Pool(processes=16) as pool:  # 根据需要设置进程数!!!!!!!
            alive_ips = pool.map(submit, (flag_list, [api for _ in flag_list], [token for _ in flag_list]))
    else:
        print('Man! Where is your flag?')
