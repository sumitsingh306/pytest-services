import pytest

from aws.elb.resources import elbs_with_attrs_v2

ELBv2_ACCESS_LOG_ENABLED = 'access_logs.s3.enabled'

def does_elbv2_have_access_log(elb):
    """
    Checks if ELB has access logging enabled

    >>> does_elbv2_have_access_log({'Attributes': [{'Key': 'access_logs.s3.enabled', 'Values': 'true'}]})
    True
    >>> does_elbv2_have_access_log({'Attributes': [{'Key': 'access_logs.s3.enabled', 'Values': 'false'}]})
    False
    >>> does_elbv2_have_access_log({'Attributes': []})
    False
    """
    for attr in elb['Attributes']:
        if attr['Key'] == ELBv2_ACCESS_LOG_ENABLED:
            return attr['Value'] == "true"
    return False

@pytest.mark.elb
@pytest.mark.parametrize('elb', elbs_with_attrs_v2(), ids=lambda elb: elb['LoadBalancerName'])
def test_elb_has_access_logs(elb):
    assert does_elbv2_have_access_log(elb), \
            "ELB doesn't have access logs enabled: {0[LoadBalancerName]}".format(elb)
