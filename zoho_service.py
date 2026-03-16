import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("ZOHO_ACCESS_TOKEN")
BASE_URL = os.getenv("ZOHO_API_DOMAIN") + "/recruit/v2"

headers = {
    "Authorization": f"Zoho-oauthtoken {TOKEN}"
}


# ---------------------------
# GET JOBS
# ---------------------------
def get_jobs():

    url = f"{BASE_URL}/Job_Openings"

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return {"error": "ATS API failed", "details": response.text}

        data = response.json().get("data", [])

        jobs = []

        for job in data:
            jobs.append({
                "id": job["id"],
                "title": job.get("Job_Opening_Name"),
                "location": job.get("City"),
                "status": job.get("Job_Opening_Status", "OPEN"),
                "external_url": ""
            })

        return jobs

    except requests.exceptions.Timeout:
        return {"error": "ATS request timeout"}

    except Exception as e:
        return {"error": str(e)}


# ---------------------------
# CREATE CANDIDATE
# ---------------------------
def create_candidate_application(payload):

    try:

        url = f"{BASE_URL}/Candidates"

        data = {
            "data": [
                {
                    "Last_Name": payload["name"],
                    "Email": payload["email"],
                    "Phone": payload["phone"],
                    "Associated_Job_Opening": payload["job_id"]
                }
            ]
        }

        response = requests.post(url, json=data, headers=headers, timeout=10)

        result = response.json()

        if response.status_code not in [200, 201]:
            return {
                "error": "Failed to create candidate",
                "details": result
            }

        candidate = result["data"][0]

        if candidate["status"] == "error":
            return {"error": candidate}

        return {
            "id": candidate["details"]["id"],
            "candidate_name": payload["name"],
            "email": payload["email"],
            "status": "APPLIED",
            "job_id": payload["job_id"]
        }

    except requests.exceptions.Timeout:
        return {"error": "ATS request timeout"}

    except Exception as e:
        return {"error": str(e)}


# ---------------------------
# GET APPLICATIONS
# ---------------------------
def get_applications(job_id=None, page=1, per_page=10):

    url = f"{BASE_URL}/Candidates"

    params = {
        "page": page,
        "per_page": per_page
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            return {
                "error": "ATS API failed",
                "details": response.text
            }

        result = response.json()

        data = result.get("data", [])

        applications = []

        for c in data:

            if job_id and str(c.get("Associated_Job_Opening")) != str(job_id):
                continue

            applications.append({
                "id": c.get("id"),
                "candidate_name": c.get("Full_Name"),
                "email": c.get("Email"),
                "status": "APPLIED"
            })

        return {
            "page": page,
            "per_page": per_page,
            "applications": applications
        }

    except requests.exceptions.Timeout:
        return {"error": "ATS request timeout"}

    except Exception as e:
        return {"error": str(e)}