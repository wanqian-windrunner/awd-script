import paramiko
import os
from data_process import Config

class ssh_connect:

    def __init__(self):
        config = Config()
        # SSH服务器的信息
        self.host = config.host
        self.port = config.port
        self.username = config.username
        self.password = config.password

        # 连接SSH服务器
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.username, self.password)

    # 打包web目录
    def pack_web(self):
        self.ssh.exec_command('cd /var/www/html')
        self.stdin1, self.stdout1, self.stderr1 = self.ssh.exec_command('tar -zcvf /tmp/html.tar.gz *')
        self.stdout1.channel.recv_exit_status()
        print(self.stderr1.read().decode())

    # 打包home目录
    def pack_home(self):
        self.ssh.exec_command('cd /home')
        self.stdin2, self.stdout2, self.stderr2 = self.ssh.exec_command('tar -zcvf /tmp/pwn.tar.gz *')
        self.stdout2.channel.recv_exit_status()
        print(self.stderr2.read().decode())

    def close(self):
        self.ssh.close()

class sftp_connect:
    def __init__(self):
        config = Config()
        # SSH服务器的信息
        self.host = config.host
        self.port = config.port
        self.username = config.username
        self.password = config.password

        # 连接SFTP服务器
        self.transport = paramiko.Transport((self.host, self.port))
        self.transport.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
    # 下载打包后的文件
    def download(self):
        remote_path = '/tmp/html.tar.gz'
        local_path = 'html.tar.gz'
        self.sftp.get('/tmp/html.tar.gz', 'html.tar.gz')
        self.sftp.get('/tmp/pwn.tar.gz', 'pwn.tar.gz')
        self.sftp.close()
        self.transport.close()
        print("文件下载完成！")
if __name__ == '__main__':
    ssh = ssh_connect()
    ssh.pack_web()
    ssh.pack_home()
    ssh.close()
    sftp = sftp_connect()
    sftp.download()
