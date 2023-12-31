import boto3

service_name = 's3'
region_name = 'eu-north-1'
bucket_name = 'devansh-mybucket-v1'
file_key = 'first text.txt'

s3 = boto3.client(service_name, region_name=region_name)

try:
    
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    
   
    file_contents = response['Body'].read().decode('utf-8')

   
    print(f'File Key: {file_key}')
    print(f'File Size: {len(file_contents)} bytes')
    print(f'Last Modified: {response["LastModified"]}')
    print(f'File Contents:')
    print(file_contents)

except Exception as e:
    print(f'An error occurred: {str(e)}')
