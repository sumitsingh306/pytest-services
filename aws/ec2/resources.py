

from conftest import botocore_client


def ec2_security_groups():
    "http://botocore.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_security_groups"
    return botocore_client\
      .get('ec2', 'describe_security_groups', [], {})\
      .extract_key('SecurityGroups')\
      .flatten()\
      .values()

def ec2_network_acls():
    "http://botocore.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_network_acls"
    return botocore_client\
      .get('ec2', 'describe_network_acls', [], {})\
      .extract_key('NetworkAcls')\
      .flatten()\
      .values()

def ec2_subnets(vpc_id):
    "http://botocore.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_subnets"
    return botocore_client\
      .get('ec2', 'describe_subnets', [], {'Filters': [{'Name': 'vpc-id', 'Values': [vpc_id]}]})\
      .extract_key('Subnets')\
      .flatten()\
      .values()

# TODO: This implementation makes n calls for n resources, where it really can make 1 call for n resources.
def ec2_flow_logs_for_resource(resource_id):
    "http://botocore.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_flow_logs"
    return botocore_client\
      .get('ec2', 'describe_flow_logs', [], {'Filters': [{'Name': 'resource-id', 'Values': [resource_id]}]})\
      .extract_key('FlowLogs', default=[])\
      .flatten()\
      .values()

def ec2_subnets_with_flow_logs(vpc_id):
    subnets = ec2_subnets(vpc_id)
    return [
        {**{'FlowLogs': ec2_flow_logs_for_resource(subnet['SubnetId'])}, **subnet} for subnet in subnets
    ]

def ec2_vpcs():
    "http://botocore.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_vpcs"
    return botocore_client\
      .get('ec2', 'describe_vpcs', [], {})\
      .extract_key('Vpcs')\
      .flatten()\
      .values()

def ec2_vpcs_with_subnets_and_flow_logs():
    return [
        {
            **{'FlowLogs': ec2_flow_logs_for_resource(vpc['VpcId'])},
            **{'Subnets': ec2_subnets_with_flow_logs(vpc['VpcId'])},
            **vpc,
        } for vpc in ec2_vpcs()
    ]
