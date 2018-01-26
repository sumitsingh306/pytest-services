
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

