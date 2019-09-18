import gzip
import json
import base64
import boto3

from botocore.vendored import requests
from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection

region = 'us-east-2'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://vpc-test-es-domain-ulyromkp7ikazf6jskl2sc3uzu.us-east-2.es.amazonaws.com'
index = 'metadata-store'
_type = 'metadata-store-type'
url = host + '/' + index + '/' + _type + '/'

def connectES(esEndPoint):
 print ('Connecting to the ES Endpoint {0}'.format(esEndPoint))
 try:
  esClient = Elasticsearch(
   hosts=[{'host': esEndPoint, 'port': 443}],
   use_ssl=True,
   verify_certs=False,
   ssl_show_warn=False)
   # connection_class=RequestsHttpConnection)
  return esClient
 except Exception as E:
  print("Unable to connect to {0}".format(esEndPoint))
  print(E)
  exit(3)

def createIndex(esClient):
 indexDoc = {
    "settings": {
     "number_of_shards": 1,
      "number_of_replicas": 0
    }
 }
 try:
  res = esClient.indices.exists('metadata-store')
  print("Index Exists ... {}".format(res))
  if res is False:
   esClient.indices.create('metadata-store', body=indexDoc)
   return 1
 except Exception as E:
  print("Unable to Create Index {0}".format("metadata-store"))
  print(E)
  exit(4)
  
def create_index():
    es = connectES('vpc-test-es-domain-ulyromkp7ikazf6jskl2sc3uzu.us-east-2.es.amazonaws.com')
    createIndex(es)
    # print('Creating index: %s' % (host + index))
    # r = requests.put(host + index, auth=awsauth)
    # print('Create index returned: %s' % r)

def put_event_to_es(event):
    print('Entering put_event_to_es')
    _id = event['id']
    timestamp = event['timestamp']
    message = event['message']
    document = {'id': _id, 'timestamp': timestamp, 'message': message.strip()}
    print('Posting document to: %s' % (url + _id))
    r = requests.post(url + _id, auth=awsauth, json=document, headers={'Content-Type': 'application/json'})
    # r = requests.put(url + _id, json=document, headers={'Content-Type': 'application/json'})
    print('Document pushed to ES: %s' % r)

def indexDocElement(esClient, event):
  try:
   _id = event['id']
   timestamp = event['timestamp']
   message = event['message']
   document = {'id': _id, 'timestamp': timestamp, 'message': message}
   retval = esClient.index(index='metadata-store', body=document)
  except Exception as E:
    print("Doc not indexed")
    print("Error: ",E)
    exit(5)

def lambda_handler(event, context):
    # print(f'Logging Event: {event}')
    # print(f"Awslog: {event['awslogs']}")
    cw_data = event['awslogs']['data']
    # print(f'data: {cw_data}')
    # print(f'type: {type(cw_data)}')
    compressed_payload = base64.b64decode(cw_data)
    uncompressed_payload = gzip.decompress(compressed_payload)
    payload = json.loads(uncompressed_payload)

    log_events = payload['logEvents']
    # create_index()
    es = connectES('vpc-test-es-domain-ulyromkp7ikazf6jskl2sc3uzu.us-east-2.es.amazonaws.com')
    createIndex(es)
    for log_event in log_events:
        # print(type(log_event))
        print(f'LogEvent: {log_event}')
        indexDocElement(es, log_event)
