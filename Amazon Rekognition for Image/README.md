Amazon Rekognition Instruction
===

Amazon Rekognition is a platform for AWS users to detect the content of image. You can use it to detect face, enviroment, etc. If you have URL of an image, use Rekognition Console and follow the instruction. If you have image file on your local device, follow the steps. 
1. Install `boto3`
```
pip install boto3
pip3 install boto3
```
#2. Install AWS CLI and configure credentials file in AWS account by creating IAM user in AWS account.
```
pip install awscli
pip3 install awscli
```
#3. In Amazon S3 website, create bucket and upload photo file in the bucket. Or you can upload photo from your Python command.
You can also create bucket and upload photos on your device by using `boto3`.
print out bucket name
```
import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
```
upload file in the bucket
```
data = open('file name', 'rb')
s3.Bucket('bucket name').put_object(Key='test.jpg', Body=data)
```
#4. Detect the photo uploaded using `boto3` package and `json` package.


References:
https://docs.aws.amazon.com/zh_cn/rekognition/latest/dg/setting-up.html
