import boto3
import logging
import gzip
import io


# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

client = None

def enter_exit_fn_log(func):
    def decorated_func(*args, **kwargs):
        print("Entering %s" % func.__name__)
        result = func(*args, **kwargs)
        print("Exiting %s" % func.__name__)
        return result
    return decorated_func

@enter_exit_fn_log
def assume_role():
    # Create IAM client
    sts_default_provider_chain = boto3.client('sts')

    print('Default Provider Identity: : ' + sts_default_provider_chain.get_caller_identity()['Arn'])

    role_to_assume_arn='arn:aws:iam::227799707625:role/assume-s3-role'
    role_session_name='test_session'

    response=sts_default_provider_chain.assume_role(
        RoleArn=role_to_assume_arn,
        RoleSessionName=role_session_name
    )

    creds=response['Credentials']

    sts_assumed_role = boto3.client('s3',
        aws_access_key_id=creds['AccessKeyId'],
        aws_secret_access_key=creds['SecretAccessKey'],
        aws_session_token=creds['SessionToken'],
    )

    # print('AssumedRole Identity: ' + sts_assumed_role.get_caller_identity()['Arn'])
    # print(dir(sts_assumed_role))
    return sts_assumed_role

@enter_exit_fn_log
def list_bucket_objects(bucket_name):
    client = boto3.client('s3')
    print(client.list_objects(Bucket=bucket_name)['Name'])

@enter_exit_fn_log
def get_object_content(bucket_name, key, client):
    # client = boto3.client('s3')
    response = client.get_object(Bucket=bucket_name, Key=key)
    gzipfile = io.BytesIO(response['Body'].read())
    gzipfile = gzip.GzipFile(fileobj=gzipfile)
    content = gzipfile.read()
    print(content)

@enter_exit_fn_log
def parse_trigger_data(record):
    if not isinstance(record, dict):
        print('Expected dictionary')
        return None
    try:
        data = {
            'bucket_name': record['s3']['bucket']['name'],
            'key': record['s3']['object']['key'],
        }
    except KeyError as e:
        print(e)
        return None
    if not (data['key'].startswith('AWSLogs/') and
            data['key'].endswith('.gz') and
            'vpcflowlogs' in data['key']):
        print('Key is not valid: %r' % data['key'])
        return None
    return data

@enter_exit_fn_log
def lambda_handler(event, context):
    for record in event['Records']:
        data = parse_trigger_data(record)
        if data is None:
            continue
        assumed_role_id = assume_role()
        list_bucket_objects(data['bucket_name'])
        get_object_content(data['bucket_name'], data['key'], assumed_role_id)
