import os

# boto3 is a library that allows Python developers to write software that makes use of Amazon services like S3 and EC2 
# but it can also be used to interact with other cloud providers like DigitalOcean Spaces.
import boto3

# openia local library is used to interact with the OpenAI API.
from open_ia import generate_image

def download_file(file_name, bucket_name, client):
    try:
        response = client.get_object(
            Bucket=bucket_name,
            Key=file_name
        )
        return response['Body'].read()
    except Exception as e:
        print(f"Error downloading file: {e}")


def main(event):

    session = boto3.session.Session()
    client = session.client('s3',
                            region_name=os.environ.get('REGION_NAME'),
                            endpoint_url=os.environ.get('ENDPOINT_URL'),
                            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
    )

    file_name = event.get("image", None)
    if file_name is None:
        return {
            "statusCode": 400,
            "body": "Missing image parameter"
        }
    image_bytes = download_file(file_name, "testfunction", client)
    
    # free memory    
    del client
    del session

    # Generate the image using the OpenAI API
    image_url = generate_image(image_bytes)

    return {
        "headers": { "Content-Type": "application/json" },
        "statusCode": 200,
        "body": {"url":image_url}
    }