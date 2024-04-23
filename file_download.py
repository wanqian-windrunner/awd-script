import paramiko
import os

# SSH服务器的信息
host = 'your_ssh_host'
port = 2222
username = 'your_ssh_username'
password = 'your_ssh_password'

# 连接SSH服务器
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# 执行打包命令
stdin, stdout, stderr = ssh.exec_command('tar czf /tmp/html.tar.gz /var/www/html')

# 等待命令执行完毕
stdout.channel.recv_exit_status()

# 关闭SSH连接
ssh.close()

# 下载打包后的文件
transport = paramiko.Transport((host, port))
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

remote_path = '/tmp/html.tar.gz'
local_path = 'html.tar.gz'

sftp.get(remote_path, local_path)

# 关闭SFTP连接
sftp.close()
transport.close()

print("文件下载完成！")
