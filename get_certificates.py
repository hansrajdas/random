# acm-pca:GetCertificateAuthorityCertificate


import json
import boto3


def lambda_handler(event, context):
  client = boto3.client('acm-pca')
  arn = 'arn:aws:acm-pca:us-east-2:288986641792:certificate-authority/19bf58d8-cc87-431f-a7c7-558f2f765318'
  data = client.get_certificate_authority_certificate(CertificateAuthorityArn=arn)
  print data
