## Dotfiles for Price Delta Tracker on AWS EC2

Dotfile for EC2 that spins up and configures virtual machines in different geographic locations to find differences in flight prices using Selenium

#### Step 1 - Setup

I'm assuming that you have followed the instructions from the other README going forward

1) First step, create an Amazon AWS account. Do not worry - AWS gives you 750 hours free of EC2 instances wherever you see the `Free tier eligible` badge on their console.

2) Get an AWS Access Key ID and AWS Secret Access Key. Access keys consist of an access key ID (for example, AKIAIOSFODNN7EXAMPLE) and a secret access key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY).
Be very careful with your keys!!! Do not push them up to github. 

3) Create a `credentials.py` file and use a dictionary to hold your keys. Then, create a `.gitignore` file and place `credentials.py` into the file so that you never accidentally push up your credentials. In the future, whenever you need to use your credentials in your code to work with the AWS CLI, you can import the credentials file where your credentials are accessible globally.


#### Step 2 - Install and configure AWS CLI

1) `$ pip3 install awscli` to install the AWS CLI

2) `$ aws configure` - this will allow you to set up your credentials and settings. You will be prompted for your (1) AWS Access Key ID (2) AWS Secret Access Key (3) Default region name, which you will this time type `us-east-2` and (4) Default output format, which you set to `json`.

So what does this all do? It allows us to interact with the AWS API which uses our Access Key ID and Secret Access Key to allow us to create instances without having to go on the Console and manually click around. This time around we have declared to AWS that we want to spin up instances in the `us-east-2` region and that all of our outputs will return in json format.

#### Step 3 - Create a Security Group and Key Pair

Now we are going to create a 'Security Group' and Key Pair - this is not the same key pair as our credentials. Group users are like profiles that you can configure to have different admin abilities. For now we will not configure this. 

1) `$ aws ec2 create-security-group --group-name super_powerful_admin --description "security group for with unlimited capabilities"`

2) `$ aws ec2 authorize-security-group-ingress --group-name super_powerful_admin --protocol tcp --port 22 --cidr 0.0.0.0/0`

Will automate this step with `setup.py`

