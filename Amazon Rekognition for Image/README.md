Amazon Rekognition Instruction
===

Amazon Rekognition is a platform for AWS users to detect the content of image. You can use it to detect face, enviroment, etc. If you have URL of an image, use Rekognition Console and follow the instruction. 
If you have image file on your local device, follow the steps. 
1. Install `boto3`
-----
Python2:
```
pip install boto3
```
Python3: 
```
pip3 install boto3
```
2. Install AWS CLI and configure credentials file in AWS account by creating IAM user in AWS account.
--------
Python2
```
pip install awscli
```
Python3
```
pip3 install awscli
```
3. Create bucket and upload photo
-------
Creat bucket on Amazon S3 website first.
You can upload a file in the bucket on Amazon S3 website. Or you can upload a file by using code.

(1) print out bucket name
```
import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
```
(2) upload file in the bucket
```
data = open('file name', 'rb')
s3.Bucket('bucket name').put_object(Key='test.jpg', Body=data)
```
4. Detect the photo uploaded using `boto3` package and `json` package.
------


References:
https://docs.aws.amazon.com/zh_cn/rekognition/latest/dg/setting-up.html
