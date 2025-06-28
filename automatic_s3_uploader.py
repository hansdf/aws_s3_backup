from secrets import access_key, secret_access_key

import boto3
import os

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)
files_uploaded = 0

for my_file in os.listdir():
    if '.txt' in my_file:
        local_file_path = os.path.join(os.getcwd(), my_file)

        upload_file_bucket = 'myawsdummybucket123'
        upload_file_key = 'txts/' + str(my_file)

        print(f"Uploading {local_file_path} to s3://{upload_file_bucket}/{upload_file_key}...")
        client.upload_file(my_file, upload_file_bucket, upload_file_key)
        
        files_uploaded += 1

if files_uploaded > 0:
    print(f'Successfully uploaded {files_uploaded} file(s)!')
else:
    print('No .txt files found to upload.')