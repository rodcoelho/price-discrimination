
# File purpose: Create a Security Group and Key Pair for the EC2 Instance ( STUFF AT THE BOTTOM OF credentials.py)






##################         ##################
##################  notes  ##################
##################         ##################

# 'us-east-1' - aws ec2 create-security-group --group-name rodcoelho --description "security group for development environment"
        # aws ec2 authorize-security-group-ingress --group-name rodcoelho --protocol tcp --port 22 --cidr 0.0.0.0/0
        # aws ec2 create-key-pair --key-name rodcoelho_key --query 'KeyMaterial' --output text > devenv-key-east1.pem



# 'us-east-2'- aws ec2 create-security-group --group-name rodcoelho --description "security group for development environment"
        # aws ec2 authorize-security-group-ingress --group-name rodcoelho --protocol tcp --port 22 --cidr 0.0.0.0/0
        # aws ec2 create-key-pair --key-name rodcoelho_key --query 'KeyMaterial' --output text > devenv-key-east2.pem


# 'us-west-1' - aws ec2 create-security-group --group-name rodcoelho --description "security group for development environment"
        # aws ec2 authorize-security-group-ingress --group-name rodcoelho --protocol tcp --port 22 --cidr 0.0.0.0/0
        # aws ec2 create-key-pair --key-name rodcoelho_key --query 'KeyMaterial' --output text > devenv-key-west1.pem


# 'us-west-2' - aws ec2 create-security-group --group-name rodcoelho --description "security group for development environment"
        # aws ec2 authorize-security-group-ingress --group-name rodcoelho --protocol tcp --port 22 --cidr 0.0.0.0/0
        # aws ec2 create-key-pair --key-name rodcoelho_key --query 'KeyMaterial' --output text > devenv-key-west2.pem









# Get local ip address - better than socket import
# Will use this ip address to with line 14 for example

# from urllib.request import urlopen
# import re
# def getPublicIp():
#     data = str(urlopen('http://checkip.dyndns.com/').read())
#     # data = '<html><head><title>Current IP Check</title></head><body>Current IP Address: 65.96.168.198</body></html>\r\n'
#
#     return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)