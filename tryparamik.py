import paramiko

addr = raw_input('What is your ec2 instance address? ')
username = raw_input('What is your ec2 username? ')
password = raw_input('What is your password? ')
remote_conn = paramiko.SSHClient()
remote_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn.connect(addr, username, password, look_for_keys=False, allow_agent=False, timeout=15)
 # exploring paramiko 