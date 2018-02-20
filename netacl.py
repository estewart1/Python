import subprocess

vpcid = raw_input('What is the id of your vpc? ')
netrules = subprocess.check_netrules('aws ec2 create-network-acl --vpc-id' + vpcid, shell=True)
commands = subprocess.check_commands('aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --ingress --rule-number 10 --cidr-block 169.254.169.254/32 --protocol http --rule-action deny',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --ingress --rule-number 20 --cidr-block 169.254.169.254/32 --protocol https --rule-action deny',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --ingress --rule-number 30 --cidr-block 0.0.0.0/0 --protocol all --rule-action allow',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --ingress --rule-number 40 --cidr-block 0::/0 --protocol all --rule-action allow',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --egress --rule-number 10 --cidr-block 169.254.169.254/32 --protocol http --rule-action deny',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --egress --rule-number 20 --cidr-block 169.254.169.254/32 --protocol https --rule-action deny',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --egress --rule-number 30 --cidr-block 0.0.0.0/0 --protocol all --rule-action allow',
'aws ec2 create-network-acl-entry --network-acl-id acl-9665effe --egress --rule-number 40 --cidr-block 0::/0 --protocol all --rule-action allow')

# Will this work for blocking metadata? 