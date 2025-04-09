import boto3
import pathlib
import requests


# Connection parameters for DigitalOcean Functions
function_url = ""
auth_token = ""

# Connection parameters for DigitalOcean Spaces
region_name = ""
endpoint_url = ""
aws_access_key_id = ""
aws_secret_access_key = ""

# bucket name
bucket_name = "testfunction"


def upload_file(file_name, bucket_name, client):
    try:
        print(f"Uploading {file_name} to {bucket_name}...")
        client.upload_file(
            file_name,
            bucket_name,
            file_name
        )
        print(f"File {file_name} uploaded successfully to {bucket_name}.")
        return True
    except Exception as e:
        print(f"Error uploading file: {e}")
    
    return False


if __name__ == "__main__":

    session = boto3.session.Session()
    client = session.client(
        's3',
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    
    file_name = input("Enter the file name to upload: ")
    if not pathlib.Path(file_name).exists():
        print(f"File {file_name} does not exist.")
        exit(1)

    response = upload_file(file_name, bucket_name, client)
    if not response:
        print("File upload failed.")
        exit(1)
    
    print("Calling the function...")
    # Call the function with the file name as a parameter
    response = requests.post(
        function_url,
        headers={
            "Authorization": f"Basic {auth_token}",
            "Content-Type": "application/json"
        },
        json={
            "image": file_name,
            "bucket_name": bucket_name
        }
    )
    if response.status_code != 200:
        print(f"Function call failed: {response.text}")
        exit(1)

    print(f"Function call succeeded: {response.json()}")