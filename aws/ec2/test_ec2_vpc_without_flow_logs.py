import pytest

from aws.ec2.resources import ec2_vpcs_with_subnets_and_flow_logs

def does_vpc_have_flow_logs(ec2_vpc):
    """
    Checks if there are any FlowLogs associated to the VPC

    >> does_vpc_have_flow_logs({'FlowLogs': [0]})
    True
    >> does_vpc_have_flow_logs({'FlowLogs': []})
    False
    >> does_vpc_have_flow_logs({})
    Traceback (most recent call last):
    ...
    KeyError: 'FlowLogs'
    >>> does_vpc_have_flow_logs(0)
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not subscriptable
    >>> does_vpc_have_flow_logs(None)
    Traceback (most recent call last):
    ...
    TypeError: 'NoneType' object is not subscriptable
    """
    return bool(len(ec2_vpc['FlowLogs']))

def does_vpc_subnets_have_flow_logs(ec2_vpc):
    """
    Checks if there are any FlowLogs associated to each subnet within a VPC.
    Returns false if there are no subnets.

    >> does_vpc_subnets_have_flow_logs({'Subnets': [{'FlowLogs': [0]}]})
    True
    >> does_vpc_subnets_have_flow_logs({'Subnets': [{'FlowLogs': [0]}, {'FlowLogs': []}]})
    False
    >> does_vpc_subnets_have_flow_logs({'Subnets': [{'FlowLogs': []}]})
    False
    >> does_vpc_subnets_have_flow_logs({'Subnets': []})
    False
    >> does_vpc_subnets_have_flow_logs({})
    Traceback (most recent call last):
    ...
    KeyError: 'Subnets'
    >>> does_vpc_subnets_have_flow_logs(0)
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not subscriptable
    >>> does_vpc_subnets_have_flow_logs(None)
    Traceback (most recent call last):
    ...
    TypeError: 'NoneType' object is not subscriptable
    """
    if not len(ec2_vpc['Subnets']):
        return False

    return all([len(subnet['FlowLogs']) for subnet in ec2_vpc['Subnets']])

@pytest.mark.ec2
@pytest.mark.xfail(reason="Need to determine flow log strategy first")
@pytest.mark.parametrize('ec2_vpc', ec2_vpcs_with_subnets_and_flow_logs(), ids=lambda ec2_vpc: ec2_vpc['VpcId'])
def test_ec2_vpc_without_flow_logs(ec2_vpc):
    if not does_vpc_have_flow_logs(ec2_vpc):
        assert does_vpc_subnets_have_flow_logs(ec2_vpc), \
           'VPC with id of {0[VpcId]} does not have flow logs enabled on it or on all of its subnets'.format(ec2_vpc)
