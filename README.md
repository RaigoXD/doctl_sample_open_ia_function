# DigitalOcean Serverless Function Sample: Image Processing with OpenAI & Spaces

## Introduction

This repository demonstrates a **Python-based serverless function** on DigitalOcean that integrates multiple cloud services:
- 🖼️ **DigitalOcean Spaces** for object storage 
- 🤖 **OpenAI GPT-4o** for image analysis
- 🎨 **AI Image Generation** for style transformation

A perfect example for developers learning serverless architectures and cloud service integrations!

### Key Features
- Serverless architecture implementation
- Cloud storage integration (DO Spaces)
- AI-powered image analysis (OpenAI)
- Style transfer image generation
- End-to-end serverless workflow
- DigitalOcean App Platform deployment

## Requirements

### Core Dependencies
* **Python 3.9+** (Tested with 3.10)
* **Python Packages**:
  - `boto3` (AWS SDK for Spaces integration)
  - `openai` (OpenAI API client)
  - `requests` (HTTP client)
  - `python-dotenv` (Environment management)

### Service Accounts
* DigitalOcean Account ([Sign Up](https://cloud.digitalocean.com/registrations/new))
* OpenAI Account with API Key ([Get Key](https://platform.openai.com/))
* DigitalOcean Spaces configured ([Spaces Documentation](https://docs.digitalocean.com/products/spaces/))

### Development Tools
* doctl CLI ([Installation Guide](https://github.com/digitalocean/doctl))
* DigitalOcean Serverless Setup ([Getting Started](https://docs.digitalocean.com/products/functions/))

## Deploying the Function
## Deployment Walkthrough

```bash
# Clone repository
git clone git@github.com:RaigoXD/doctl_sample_open_ia_function.git
cd doctl_sample_open_ia_function

# Install Python dependencies (local testing)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Deploy to DigitalOcean (ensure doctl is authenticated)
doctl serverless deploy . --remote-build

# Get function URL after deployment
doctl serverless function get create_ghibli_image --url
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

## Usage Example

```bash
curl -X PUT \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic {{auth_token}}' \
  {your-function-url} \
  -d '{
    "image": "sample.jpg",
    "bucket_name": "my-anime-bucket"
  }'
```

### Learn More

You can learn more about Functions and App Platform integration in [the official App Platform Documentation](https://www.digitalocean.com/docs/app-platform/).
ContactMe: jh.raigo@gmail.com
