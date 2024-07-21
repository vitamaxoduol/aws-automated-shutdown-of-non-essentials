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

#### Stop Non-Essential Service Script
This will stop all the EC2 instances with specific tag during off-hours

#### Startup script
This will start all the EC2 instances with specific tag during working hours


### Set up the Lambda functions in AWS Management Console.
1. **Navigate to AWS Lambda:**
Go to the AWS Management Console and open the Lambda service.

2. **Create a New Function:**
- Click on "Create function".
- Choose "Author from scratch".
- Provide a name for your function:`StopNonEssentialServices`
- Choose Python 3.x as the runtime.
Set up necessary permissions by either creating a new role with basic Lambda permissions or choosing an existing role.
3. **Repeat for the Startup Script:**
- Follow the same steps to create another Lambda function: `StartNonEssentialServices`

### Deploy the Python Scripts to Lambda Functions
**Stop Non-Essential Services Script:**
- Go to the StopNonEssentialServices function in the Lambda console.
- Copy and paste the shutdown script into the code editor as provided in file `shutdown-script.py`

**Start Non-Essential Services Script:**
- Go to the StartNonEssentialServices function in the Lambda console.
- Copy and paste the startup script into the code editor as provided in file `startup-script.py`.

**Deploy the Code:**
- Click "Deploy" to save and deploy the function.

### Configure CloudWatch Events
**Create a CloudWatch Rule for Shutdown:**
- Go to the CloudWatch service in the AWS Management Console.
- Select "Rules" under the "Events" section.
- Click "Create rule".
- For the event source, choose "Event Source" as "Schedule" and set a cron expression for off-hours `cron(0 19 * * ? *)` for 7 PM.
- Add the target by selecting "Lambda function" and choose the `StopNonEssentialServices` Lambda function.
- Configure any necessary permissions and save the rule.

**Create a CloudWatch Rule for Startup:**
- Repeat the steps above to create another rule with a cron expression for working hours, `cron(0 7 * * ? *)` for 7 AM.
- Add the target by selecting "Lambda function" and choose the `StartNonEssentialServices` Lambda function.
- Configure any necessary permissions and save the rule.

**By automating these scripts, you can ensure that non-essential services are only running when needed, leading to significant cost savings.**

## License 
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for
details
