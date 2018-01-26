from conftest import botocore_client

def elbs():
    "http://botocore.readthedocs.io/en/latest/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancers"
    return botocore_client\
      .get('elb', 'describe_load_balancers', [], {})\
      .extract_key('LoadBalancerDescriptions')\
      .flatten()\
      .values()

def elb_attrs(elb_name):
    "http://botocore.readthedocs.io/en/latest/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_attributes"
    return botocore_client\
      .get('elb', 'describe_load_balancer_attributes', [], {'LoadBalancerName': elb_name})\
      .extract_key('LoadBalancerAttributes')\
      .values()[0]

def elbs_with_attrs():
    return [{**elb_attrs(elb['LoadBalancerName']), **elb} for elb in elbs()]
