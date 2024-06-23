import boto3

client=boto3.client('ec2')
instance_Id= input ("Enter instance ID: ")

response = client.start_instances(InstanceIds=[instance_Id],
)

print(response)