

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
