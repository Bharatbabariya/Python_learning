import boto3
import pandas as pd
import io

REGION = 'us-east-1'
ACCESS_KEY_ID = 'paste_here_your_key_id'
SECRET_ACCESS_KEY = 'paste_here_your_secret_access_key'

BUCKET_NAME = 'vperezb'
KEY = 'path/in/s3/namefile.txt' # file path in S3 

s3c = boto3.client(
        's3', 
        region_name = REGION,
        aws_access_key_id = ACCESS_KEY_ID,
        aws_secret_access_key = SECRET_ACCESS_KEY
    )

obj = s3c.get_object(Bucket= BUCKET_NAME , Key = KEY)
df = pd.read_csv(io.BytesIO(obj['Body'].read()), encoding='utf8')
df
