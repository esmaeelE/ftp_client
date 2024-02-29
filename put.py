import paramiko


# Fill Required Information
HOSTNAME = "172.16.0.10"
USERNAME = "uat"
PASSWORD = "uat"
PORT = "2796"

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(HOSTNAME, username=USERNAME, password=PASSWORD, port=PORT)
except paramiko.AuthenticationException as error:
    print("ERROR")

remote_path = "/client_pics/testfile"
local_path = "send.txt"

# Copy file over sftp
try:
    sftp = ssh.open_sftp()
    sftp.put(local_path, remote_path)
except:
    print("error in copy to remote server")

sftp.close()
ssh.close()
