# ATS Integration Microservice (Python + Serverless)

This project is a Python-based serverless microservice that integrates with Zoho Recruit ATS.
It provides REST APIs to fetch job openings, submit candidate applications, and retrieve applications.
The service is built using Python, Serverless Framework, and Zoho Recruit API.

---

# Features

* Fetch job openings from Zoho Recruit
* Submit candidate applications to ATS
* Retrieve applications for a specific job
* Pagination support
* Error handling for ATS API responses
* Environment variable configuration
* Serverless architecture using AWS Lambda

---

# Tech Stack

* Python 3.9+
* Serverless Framework
* AWS Lambda (simulated locally)
* Zoho Recruit API
* Postman (API testing)

---

# Project Structure

```
ats-integration-microservice
│
├── handler.py
├── zoho_service.py
├── serverless.yml
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# API Endpoints

## Get Jobs

```
GET /jobs
```

Example response:

```
[
 {
  "id": "214803000000369131",
  "title": "Frontend Developer",
  "location": "Delhi",
  "status": "OPEN",
  "external_url": ""
 }
]
```

---

## Create Candidate Application

```
POST /candidates
```

Example request body:

```
{
 "name": "Rahul Sharma",
 "email": "rahul@test.com",
 "phone": "9876543210",
 "resume_url": "https://drive.google.com/resume",
 "job_id": "214803000000369131"
}
```

Example response:

```
{
 "id": "123456789",
 "candidate_name": "Rahul Sharma",
 "email": "rahul@test.com",
 "status": "APPLIED",
 "job_id": "214803000000369131"
}
```

---

## Get Applications

```
GET /applications?job_id=214803000000369131
```

Example response:

```
{
 "page": 1,
 "per_page": 10,
 "applications": [
  {
   "id": "123456789",
   "candidate_name": "Rahul Sharma",
   "email": "rahul@test.com",
   "status": "APPLIED"
  }
 ]
}
```

---

# Pagination

Applications endpoint supports pagination.

Example:

```
GET /applications?page=1&per_page=10
```

---

# Setup Instructions

Follow the steps below to run this project on your system.

---

# 1. Clone the Repository

Download the project from GitHub.

```
git clone git remote add origin https://github.com/iotiangyanu/ATS-integrations-API
```

Navigate to the project folder.

```
cd ats-integration-microservice
```

---

# 2. Install Python

Ensure Python 3.9 or later is installed.

Check version:

```
python --version
```

---

# 3. Install Node.js

Serverless Framework requires Node.js.

Check installation:

```
node -v
```

---

# 4. Install Serverless Framework

```
npm install -g serverless
```

Verify installation:

```
serverless --version
```

---

# 5. Install Python Dependencies

Install required Python packages.

```
pip install -r requirements.txt
```

---

# 6. Create Zoho Recruit Account

1. Go to
   https://recruit.zoho.com

2. Create a free trial account.

3. After login, create some **Job Openings**.

Example:

```
Frontend Developer
Backend Developer
```

---

# 7. Generate Zoho OAuth Token

Go to:

```
https://api-console.zoho.com
```

Create a client.

Save the following:

```
CLIENT_ID
CLIENT_SECRET
REFRESH_TOKEN
```

Generate an access token using postman:

```
POST https://accounts.zoho.com/oauth/v2/token
```

Body:

```
refresh_token=YOUR_REFRESH_TOKEN
client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
grant_type=refresh_token
```

Response:

```
{
 "access_token": "1000.xxxxxxxxxxxxxx",
 "expires_in": 3600
}
```

---

# 8. Configure Environment Variables

Create a `.env` file.

Example:

```
ZOHO_ACCESS_TOKEN=1000.xxxxxxxxxxxxxx
ZOHO_API_DOMAIN=https://recruit.zoho.com
```

---

# 9. Run the Service Locally

Start the serverless offline environment.

```
serverless offline
```

Server will start at:

```
http://localhost:3000
```

---

# 10. Test APIs Using Postman

Example requests.

Get Jobs:

```
GET http://localhost:3000/dev/jobs
```

Create Candidate:

```
POST http://localhost:3000/dev/candidates
```

Body:

```
{
 "name": "Rahul Sharma",
 "email": "rahul@test.com",
 "phone": "9876543210",
 "resume_url": "https://drive.google.com/resume",
 "job_id": "214803000000369131"
}
```

Get Applications:

```
GET http://localhost:3000/dev/applications
```

Pagination Example:

```
GET http://localhost:3000/dev/applications?page=1&per_page=5
```

---

# Error Handling

The service returns clean JSON errors if the ATS API fails.

Example:

```
{
 "error": "ATS API failed",
 "details": "Invalid OAuth token"
}
```

---

# Run Tests

Insert sample candidate applications using the POST endpoint and retrieve them using the GET endpoint.

---

# Notes

* Ensure the Zoho OAuth token is valid.
* Access tokens expire periodically and must be refreshed.

---

# Author
Gyanesh Dwivedi
