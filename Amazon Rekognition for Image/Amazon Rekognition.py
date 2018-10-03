import boto3
import json
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
data = open('file name', 'rb')
s3.Bucket('bucket name').put_object(Key='test.jpg', Body=data)
if ___name___ == "__main__":
        photo = 'file name'
        bucket = 'bucket name'
        client = boto3.client('rekognition')

        response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': photo}}, Attributes=['ALL'])

        print('Detected faces for ' + photo)    
        for faceDetail in response['FaceDetails']:
              print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
                    + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
              print('Here are the other attributes:')
              print(json.dumps(faceDetail, indent=4, sort_keys=True))

