import pytest

from aws.elb.resources import elbs_with_attrs
from aws.elb.helpers import does_elb_have_access_log

@pytest.mark.elb
@pytest.mark.parametrize('elb', elbs_with_attrs(), ids=lambda elb: elb['LoadBalancerName'])
def test_elb_has_access_logs(elb):
    assert does_elb_have_access_log(elb), \
            "ELB doesn't have access logs enabled: {0[LoadBalancerName]}".format(elb)
