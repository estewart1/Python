"""from firewall import *
single = Firewall()
single.policy(single.INPUT,single.DROP)
single.input().protocol('http').destination('169.254.169.254').drop()
single.show()
#single.run()
#single.list()
print()
"""

netsh advfirewall firewall add rule name = "BlockMetaData" protocol=HTTP dir=out remoteport=80 action=block
netsh advfirewall firewall add rule name = "BlockMetaData" protocol=HTTP dir=in remoteport=80 action=block