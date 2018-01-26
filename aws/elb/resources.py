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

def elbs_v2():
    "http://botocore.readthedocs.io/en/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancers"
    return botocore_client\
      .get('elbv2', 'describe_load_balancers', [], {})\
      .extract_key('LoadBalancers')\
      .flatten()\
      .values()

def elb_attrs_v2(elb_arn):
    "http://botocore.readthedocs.io/en/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancer_attributes"
    return botocore_client\
      .get('elbv2', 'describe_load_balancer_attributes', [], {'LoadBalancerArn': elb_arn})\
      .extract_key('Attributes')\
      .flatten()\
      .values()

def elbs_with_attrs_v2():
    return [{**{'Attributes': elb_attrs_v2(elb['LoadBalancerArn'])}, **elb} for elb in elbs_v2()]
