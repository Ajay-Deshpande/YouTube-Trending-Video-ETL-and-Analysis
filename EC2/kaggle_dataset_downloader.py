import kagglehub
import sys
import os
import boto3
from glob import glob
import shutil

s3_client = boto3.client('s3')
key_bucket = os.environ.get('KAGGLE_KEY_BUCKET')
s3_client.download_file(key_bucket, "kaggle.json", '.kaggle/kaggle.json')

path = kagglehub.dataset_download(os.environ.get("KAGGLE_DATASET_NAME"))

dataset_bucket = os.environ.get("DESTINATION_BUCKET")

for file_name in glob(os.path.join(path, '*')):
    file_str = file_name.split('/')[-1]
    if file_str.endswith('json'):
        s3_client.upload_file(file_name, dataset_bucket, f"raw_data/json_data/{file_str}")
    elif file_str.endswith('csv'):
        region = file_str[:2]
        s3_client.upload_file(file_name, dataset_bucket, f"raw_data/csv_data/Region={region}/{file_str}")
    
    print(file_str, "uploaded")

shutil.rmtree(path)
