import boto3

client = boto3.client('ec2')
instance_Id= input ("Enter instance ID: ")

response = client.stop_instances(InstanceIds=[instance_Id])


print(response)