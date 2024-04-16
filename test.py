import boto3

# Create a boto3 EC2 resource
ec2 = boto3.resource('ec2', region_name='us-east-1')

# Create a new EC2 instance
instances = ec2.create_instances(
    ImageId='ami-051f8a213df8bc089',  # AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  #instance type
    KeyName='test',  # key pair name
    TagSpecifications=[ #tags for creating instance
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'pythontestdeploy'  # The name to assign to instance
                }
            ]
        }
    ]
)
