import paramiko
import os
from data_process import Config

class ssh_connect:

    def __init__(self,config):

        # SSH服务器的信息
        self.host = config.host
        self.port = config.port
        self.username = config.user
        self.password = config.passwd

        # 连接SSH服务器
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print('\n\nip地址:', self.host, '端口:', self.port, '用户名:', self.username, '密码:', self.password)
        self.ssh.connect(self.host, int(self.port), self.username, self.password)

    # 打包web目录
    def pack_web(self):
        self.ssh.exec_command('cd /var/www/html')
        self.stdin1, self.stdout1, self.stderr1 = self.ssh.exec_command('tar -zcvf /tmp/html.tar.gz /var/www/html/*')
        self.stdout1.channel.recv_exit_status()
        print(self.stderr1.read().decode())

    # 复制pwn
    def cp_pwn(self):
        print('正在复制pwn文件到/tmp目录')
        self.stdin2, self.stdout2, self.stderr2 = self.ssh.exec_command('cp /home/ctf/pwn /tmp/pwn')
        self.stdout2.channel.recv_exit_status()
        print(self.stderr2.read().decode())

    def close(self):
        self.ssh.close()

class sftp_connect:
    def __init__(self,config):

        # SSH服务器的信息
        self.host = config.host
        self.port = config.port
        self.username = config.user
        self.password = config.passwd

        # 连接SFTP服务器
        self.transport = paramiko.Transport((self.host, int(self.port)))
        self.transport.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
    # 下载打包后的文件
    def download(self):
        self.sftp.get('/tmp/html.tar.gz', 'html.tar.gz')
        print('开始下载web附件，请稍等')
        self.sftp.get('/tmp/pwn', 'pwn')
        print('开始下载web附件，请稍等')
        self.sftp.close()
        self.transport.close()
        print("文件下载完成！")
    def close(self):
        self.sftp.close()
        self.transport.close()
        
if __name__ == '__main__':
    ssh = ssh_connect()
    ssh.pack_web()
    ssh.pack_home()
    ssh.close()
    sftp = sftp_connect()
    sftp.download()
