import boto3
import pathlib
import requests


# Connection parameters for DigitalOcean Functions
function_url = "https://faas-nyc1-2ef2e6cc.doserverless.co/api/v1/namespaces/fn-229fd9a0-2811-426a-8cbd-08f529d15116/actions/sample/create_ghibli_image?blocking=true&result=true"
auth_token = "M2Q2NzRlOWEtN2RmOS00MzU0LThjYWQtN2VhNGVmZWUxNmRmOjAwSjRJdVpiaXY3TVFIMVFCbDVNbUFJSkNYck1zVmZhVXN4Mk5lc1oxWTdJdEcyN3RWRWFPdGVNMXI5dnVmejc"

# Connection parameters for DigitalOcean Spaces
region_name = "nyc3"
endpoint_url = "https://nyc3.digitaloceanspaces.com"
aws_access_key_id = "DO00E7UYYK6Z8FV7PQ3P"
aws_secret_access_key = "Wo1CHUYLahi7J2lu47g+YqeBAlOm68T8Xo9uYd+lK6U"

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