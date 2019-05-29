import boto3
import json
import telnetlib


def check_alive_using_telnet(host, port):
  telnet = telnetlib.Telnet()
  status = '0'
  try:
    telnet.open(host, port, timeout=3)
    status = '1'
    print('%s:%s is Running' % (host, port))
  except Exception as e:
    print('%s:%s is Down' % (host, port))
  finally:
    telnet.close()
  return status
      
def lambda_handler(event, context):
  cloudwatch = boto3.client('cloudwatch')
  metric_data = [{
    'MetricName': 'LB Response',
    'Dimensions': [{
      'Name': 'Hostname',
      'Value': 'localhost:22',
    },
    {
      'Name': 'Status',
      'Value': 'Running',
    }],
    'Unit': 'None',
    'Value': 0
  }]
  
  # Call check alive function with sample data. 
  configs = [
    ('localhost', 80),
    ('localhost', 22),
    ('login.gs.com', 80),
    ('login.gs.com', 443),
    ('www.google.com', 443),
    ('10.10.10.189', 22),
    ('18.216.6.240', 22),
  ]
  for config in configs:
    status = check_alive_using_telnet(config[0], config[1])
    metric_data[0]['Dimensions'][0]['Value'] = '{0}:{1}'.format(config[0], config[1])
    metric_data[0]['Dimensions'][1]['Value'] = status
    reponse = cloudwatch.put_metric_data(MetricData=metric_data, Namespace='LBExternalChecks')
    print reponse
