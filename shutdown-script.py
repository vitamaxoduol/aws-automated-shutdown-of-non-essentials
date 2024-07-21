import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Initialize a session using Amazon EC2
    ec2 = boto3.client('ec2')

    # Define the tag key and value for non-essential services
    tag_key = 'Environment'
    tag_value = 'NonEssential'

    # Define the off-hours (example: 7 PM to 7 AM)
    off_hours_start = 19
    off_hours_end = 7

    # Get current hour
    current_hour = datetime.now().hour

    # Check if it's off-hours
    if current_hour >= off_hours_start or current_hour < off_hours_end:
        # Find all instances with the specified tag
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

        # Extract instance IDs
        instance_ids = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])

        # Stop instances
        if instance_ids:
            print(f"Stopping instances: {instance_ids}")
            ec2.stop_instances(InstanceIds=instance_ids)
        else:
            print("No instances to stop.")
    else:
        print("It's not off-hours. No action taken.")