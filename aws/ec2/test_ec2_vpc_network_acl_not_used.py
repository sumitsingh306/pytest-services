import pytest

from aws.ec2.resources import ec2_network_acls

def is_ec2_network_acl_in_use(ec2_network_acl):
    """
    Checks the Network ACL for Associations and for if it is the default for it's VPC.

    >> is_ec2_network_acl_in_use({'Associations': [0], 'IsDefault': False})
    True
    >> is_ec2_network_acl_in_use({'Associations': [], 'IsDefault': True})
    True
    >> is_ec2_network_acl_in_use({'Associations': [], 'IsDefault': False})
    False
    >> is_ec2_network_acl_in_use({})
    Traceback (most recent call last):
    ...
    KeyError: 'Associations'
    >> is_ec2_network_acl_in_use(None)
    Traceback (most recent call last):
    ...
    TypeError: 'NoneType' object is not subscriptable
    """
    if len(ec2_network_acl['Associations']) > 0 or ec2_network_acl['IsDefault']:
        return True
    return False

@pytest.mark.ec2
@pytest.mark.parametrize(
        'ec2_network_acl',
        ec2_network_acls(),
        ids=lambda ec2_network_acl: ec2_network_acl['NetworkAclId'])
def test_ec2_network_acl_all_ports(ec2_network_acl):
    assert is_ec2_network_acl_in_use(ec2_network_acl)
