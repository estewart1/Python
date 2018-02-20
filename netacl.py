import subprocess
import paramiko
import sys
import iptc

ip = raw_input('What is your ec2 instance address? ')
port = 22
username = 'ec2-user'
key = paramiko.RSAKey.from_private_key_file(raw_input("What is the path to your private key? "))
cmd = 'nc -zv 169.254.169.254 80'


def sshing():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,pkey=key)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    stdin,stdout,stder = ssh.exec_command('echo $PATH')
    x = stdout.readlines()
    return ''.join(x)
print(sshing())

vpcid = raw_input('What is the id of your vpc? ')

netrules = subprocess.check_call('aws ec2 create-network-acl --vpc-id' + vpcid, shell=True)
commands = subprocess.check_call('aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --ingress --rule-number 10 --cidr-block 169.254.169.254/32 --protocol http --rule-action deny',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --ingress --rule-number 20 --cidr-block 169.254.169.254/32 --protocol https --rule-action deny',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --ingress --rule-number 30 --cidr-block 0.0.0.0/0 --protocol all --rule-action allow',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --ingress --rule-number 40 --cidr-block 0::/0 --protocol all --rule-action allow',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --egress --rule-number 10 --cidr-block 169.254.169.254/32 --protocol http --rule-action deny',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --egress --rule-number 20 --cidr-block 169.254.169.254/32 --protocol https --rule-action deny',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --egress --rule-number 30 --cidr-block 0.0.0.0/0 --protocol all --rule-action allow',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --egress --rule-number 40 --cidr-block 0::/0 --protocol all --rule-action allow')

# Will this work for blocking metadata? 