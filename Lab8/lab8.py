from email.mime.text import MIMEText

import boto3
import redis
import smtplib
from email.message import EmailMessage

def test_minio():
    print("MinIO Web UI: http://localhost:9001")
    print("MinIO User: minioadmin")
    print("MinIO password: minioadmin123")

    s3 = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='minioadmin',
        aws_secret_access_key='minioadmin123',
    )
    try:
        s3.create_bucket(Bucket="lab8")
    except s3.exceptions.BucketAlreadyOwnedByYou:
        pass
    except s3.exceptions.BucketAlreadyExists:
        pass

    s3.put_object(Bucket="lab8", Key="test_lab8", Body="test")

def test_redis():
    print("Redis:")
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('mykey', 'Hello World')
    val = r.get('mykey').decode()
    print("Redis mykey:", val)

def test_email():
    print("Email Server:")
    print("http://localhost:8025/")

    body = "Test email for Lab8."
    msg = MIMEText(body)
    msg["From"] = "test@example.com"
    msg["To"] = "recipient@example.com"
    msg["Subject"] = "test"

    try:
        with smtplib.SMTP("localhost", 1025) as server:
            server.sendmail("test@example.com", ["rec_test@example.com"], msg.as_string())
        print("email sent")
    except Exception as e:
        print(f"email failed to send", e)

if __name__ == '__main__':
    test_minio()
    test_email()
    test_redis()
