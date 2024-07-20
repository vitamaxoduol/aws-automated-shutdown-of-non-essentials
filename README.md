# aws-automated-shutdown-of-non-essentials
- Python scripts to automate the shutdown and startup of non-essential services in AWS using Boto3, the AWS SDK for Python. 
- These scripts assume you are dealing with EC2 instances, but similar concepts can be applied to other services.
- The scripts are designed to be run as cron jobs on a regular basis, and can be configured
to run at different times of the day or week.
- The scripts use the AWS CLI to interact with the AWS API, and require the AWS CLI to
be installed and configured on the machine running the scripts.
- The scripts also require the Boto3 library to be installed, which can be done using pip
install boto3.
- The scripts are designed to be run on a Linux or Unix machine, but can be adapted to
run on Windows machines with some modifications.
- The scripts are designed to be run as root or with sudo privileges, as they require
access to the AWS CLI and Boto3 libraries.
- The scripts are designed to be run on a machine that has access to the internet, as
they require access to the AWS API.


## Problem Case:
Automated Shutdown of Non-Essential Services:

1. Identified non-critical services and environments that were not required during off-hours (e.g., development and testing environments).
2. Develope and deploye automation scripts to schedule the shutdown of these services during nights and weekends.
3. Implemented start-up scripts to ensure services were available during working hours, minimizing disruption.
4. Conducted regular reviews to ensure the shutdown schedule was up-to-date and accurate.

## Prerequisites
- AWS CLI installed and configured on the machine running the scripts.
- Boto3 library installed on the machine running the scripts: 
`pip install boto3`
- AWS Credentials: Make sure your AWS credentials are configured. You can set them up using the AWS CLI or by configuring environment variables.

### Shutdown script
This will stop all the EC2 instances with specific tag during off-hours


### Startup script
This will start all the EC2 instances with specific tag during working hours

### Scheduling the Scripts
To automate the execution of these scripts, you can use a scheduling service such as AWS Lambda with CloudWatch Events or an EC2 instance with cron jobs.

    #### Using AWS Lambda and CloudWatch Events
    1. **Create Lambda Functions:** Deploy the shutdown and startup scripts as separate Lambda functions.

    2. **Create CloudWatch Rules:**
    - Shutdown Rule: Schedule the shutdown Lambda function to run at the beginning of off-hours.
    - Startup Rule: Schedule the startup Lambda function to run at the beginning of working hours.
    **To explain of how you might create these schedules using the AWS Management Console:**

    - Shutdown Schedule: Create a rule with a cron expression like cron(0 19 * * ? *) for 7 PM.
    - Startup Schedule: Create a rule with a cron expression like cron(0 7 * * ? *) for 7 AM.
By automating these scripts, you can ensure that non-essential services are only running when needed, leading to significant cost savings.