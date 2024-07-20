import boto3
from datetime import datetime

# Intitialize the a session using Amazon EC2
ec2 = boto3.client('ec2')

# # Intitialize the a session using Amazon S3
# s3 = boto3.client('s3')

# s3_resource = boto3.resource('s3')
# bucket = s3_resource.Bucket('mybucket')
# bucket.create()
# bucket.upload_file('test.txt', 'test.txt')
# bucket.download_file('test.txt', 'test.txt')
# bucket.delete()

# Define the tag key and value for non-essential services
tag_key = 'Environment'
tag_value = 'NonEssential'

# Define the working hours
working_hours_start = 7
working_hours_end = 19

# Get the current hour
current_hour = datetime.now().hour
print(current_hour)

# Check if it's working hours
if working_hours_start <= current_hour < working_hours_end:
    # Get all running instances with the specified tag
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': f'tag:{tag_key}',
                'Values': [tag_value]
            },
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )
    # Extracting instance IDs
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
            print(instance_ids)
            
    # Stop instances
    if instance_ids:
        print(f'Stopping instances: {instance_ids}')
        ec2.stop_instances(InstanceIds=instance_ids)
    else:
        print("No instances to stop")

else:
    print("It's not off-hours. No action taken.")

