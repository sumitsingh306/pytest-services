import pytest

from aws.elb.resources import elbs_with_attrs


def does_elb_have_access_log(elb):
    """
    Checks if ELB has access logging enabled

    >>> does_elb_have_access_log({'AccessLog': {'Enabled': True}})
    True
    >>> does_elb_have_access_log({'AccessLog': {'Enabled': False}})
    False
    >>> does_elb_have_access_log({'AccessLog': {}})
    Traceback (most recent call last):
    ...
    KeyError: 'Enabled'
    >>> does_elb_have_access_log({})
    Traceback (most recent call last):
    ...
    KeyError: 'AccessLog'
    """
    return elb['AccessLog']['Enabled']

@pytest.mark.elb
@pytest.mark.parametrize('elb', elbs_with_attrs(), ids=lambda elb: elb['LoadBalancerName'])
def test_elb_has_access_logs(elb):
    assert does_elb_have_access_log(elb), \
            "ELB doesn't have access logs enabled: {0[LoadBalancerName]}".format(elb)
