import paramiko


# Fill Required Information about remote server
HOSTNAME = "172.16.0.10"
USERNAME = "uat"
PASSWORD = "uat"
PORT = "2796"

# create a client called ssh
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(HOSTNAME, username=USERNAME, password=PASSWORD, port=PORT)
    # stdin, stdout, stderr=ssh.exec_command(cmd)
except paramiko.AuthenticationException as error:
    print("ERROR in connnection")

# Download file from remoteserver
try:
    sftp = ssh.open_sftp()
    sftp.get("/pics/abc.png", "abc.png")
except:
    print("error in get")

sftp.close()
ssh.close()
