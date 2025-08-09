import boto3
import redis
import smtplib
from email.message import EmailMessage

def l8_minio():
    print("Connecting to MinIO...")
    s3 = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='minioadmin',
        aws_secret_access_key='minioadmin123',
        region_name='us-east-1'
    )

    bucket = s3.Bucket('lab8')
    file_content = "lab8_test"
    filename = 'test.txt'


    try:
        s3.create_bucket(Bucket=bucket)
    except s3.exceptions.BucketAlreadyOwnedByYou:
        pass
    except s3.exceptions.BucketAlreadyExists:
        pass

    s3.put_object(Bucket=bucket, Key=filename, Body=file_content)
    obj = s3.get_object(Bucket=bucket, Key=filename)
    data = obj['Body'].read().decode()
    print("MinIO file content:", data)

def l8_redis():
    print("Connecting to Redis...")
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('lab8_key', 'redis is working!')
    val = r.get('lab8_key').decode()
    print("Redis stored value:", val)

def l8_email():
    print("Sending email via MailHog...")
    msg = EmailMessage()
    msg['Subject'] = 'Lab 8 Test'
    msg['From'] = 'test@example.com'
    msg['To'] = 'student@example.com'
    msg.set_content('This is a test email from Lab 8.')

    with smtplib.SMTP('localhost', 1025) as smtp:
        smtp.send_message(msg)
    print("Email sent! View it at http://localhost:8025")

if __name__ == '__main__':
    l8_minio()
    l8_redis()
    l8_email()
