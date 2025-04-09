# Sample Function: Python "Open IA and Spaces Object Storage" 

## Introduction


This repository contains a image generation function written in Python using DO Space and OpenIA. You are able to send images to Spaces Storage get the description image using gtp-4o and generate a similar image with a anime style. You can deploy it on DigitalOcean's App Platform as a Serverless Function component.
Documentation is available at https://docs.digitalocean.com/products/functions.

### Requirements

* You need a DigitalOcean account. If you don't already have one, you can sign up at [https://cloud.digitalocean.com/registrations/new](https://cloud.digitalocean.com/registrations/new).
* You need a OpenIA platforma account and API_KEY. If you don't already have one, you can sign up at  https://platform.openai.com/
* To deploy from the command line, you will need the [DigitalOcean `doctl` CLI](https://github.com/digitalocean/doctl/releases).

## 📁 Project Structure

The project is organized in a simple but effective way:

- **`main.py`**: The main entry point that receives the request, downloads the image from Spaces, and coordinates the entire process.

- **`open_ia.py`**: Manages communication with OpenAI. It first obtains a detailed description of the image using GPT-4o and then uses DALL·E to create the Ghibli-style version.

- **`image_convert.py`**: Converts the image to the correct format to be processed by the OpenAI API.

- **`requirements.txt`**: Lists the dependencies needed for the function to operate correctly.

- **`build.sh`**: Script that sets up the virtual environment to deploy the function.

---

## ⚙️ How it Works

When you send a request to the function, the following happens:

1. **Image Download**:  
   The function receives the name of your image and the bucket where it's stored in Spaces. It uses `boto3` (a library for communicating with cloud storage services) to download the image.

2. **Image Analysis**:  
   The image is sent to **GPT-4o**, which analyzes it and creates a detailed description of what it contains.

3. **Art Generation**:  
   This description, along with specific instructions to create a style reminiscent of Studio Ghibli, is sent to **DALL·E 3**, which produces a new image with that characteristic style.

4. **Result**:  
   The function returns a **link to the generated image**, ready to be viewed or used.

### Integration Flow

This repository continais a folder named integration flow, this is a basic flow to use this function. 

## Deploying the Function

```bash
# clone this repo
git clone git@github.com:RaigoXD/doctl_sample_open_ia_function.git
```

```
# deploy the project, using a remote build so that compiled executable matched runtime environment
> doctl serverless deploy doctl_sample_open_ia_function --remote-build
Deploying 'doctl_sample_open_ia_function'
  to namespace 'fn-...'
  on host 'https://faas-...'
Submitted action 'create_ghibli_image' for remote building and deployment in runtime python:default (id: ...)

Deployed functions ('doctl sls fn get <funcName> --url' for URL):
  - sample/create_ghibli_image
```


### To send an email using curl:
```
curl -X PUT -H 'Content-Type: application/json' -H 'Authorization: Basic {{auth_token}}' {your-DO-app-url} -d '{"image": "{{image_name}}","bucket_name": "{{bucket_name}}"}' 
```

### Learn More

You can learn more about Functions and App Platform integration in [the official App Platform Documentation](https://www.digitalocean.com/docs/app-platform/).
ContactMe: jh.raigo@gmail.com
