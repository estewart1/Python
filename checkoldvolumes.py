import boto3
ec2 = boto3.resource('ec2',region_name='us-east-1')

def lambda_handler(event, context):
    for vol in ec2.volumes.all():
        if  vol.state=='available':
            if vol.tags is None:
                vid=vol.id
                print ("Found " + vid) 
                