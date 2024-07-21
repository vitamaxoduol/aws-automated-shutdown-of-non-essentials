import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Initialize a session using Amazon EC2
    ec2 = boto3.client('ec2')

    # Define the tag key and value for non-essential services
    tag_key = 'Environment'
    tag_value = 'NonEssential'

    # Define the working hours (example: 7 AM to 7 PM)
    work_hours_start = 7
    work_hours_end = 19

    # Get current hour
    current_hour = datetime.now().hour

    # Check if it's working hours
    if work_hours_start <= current_hour < work_hours_end:
        # Find all instances with the specified tag
        response = ec2.describe_instances(
            Filters=[
                {
                    'Name': f'tag:{tag_key}',
                    'Values': [tag_value]
                },
                {
                    'Name': 'instance-state-name',
                    'Values': ['stopped']
                }
            ]
        )

        # Extract instance IDs
        instance_ids = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])

        # Start instances
        if instance_ids:
            print(f"Starting instances: {instance_ids}")
            ec2.start_instances(InstanceIds=instance_ids)
        else:
            print("No instances to start.")
    else:
        print("It's not working hours. No action taken.")