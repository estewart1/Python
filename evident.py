import subprocess

def evident():
    permfile = '"abc.pem"' + ' '
    userandip = 'ec2-user@ec2-34-209-91-150.us-west-2.compute.amazonaws.com' + ' '
    output = subprocess.check_output('sudo ssh -i ' + permfile + userandip + '<<END nc -zv 169.254.169.254 80 END', shell=True)
#netsh advfirewall firewall add rule name = "BlockMetaData" protocol=HTTP dir=out remoteport=80 action=block
#netsh advfirewall firewall add rule name = "BlockMetaData" protocol=HTTP dir=in remoteport=80 action=block
    if 'succeeded' in output:
        return  output = subprocess.check_output('sudo ssh -i ' + permfile + userandip + '<<END (sudo pfctl -e -k 169.254.169.254) END', shell=True)
print evident()