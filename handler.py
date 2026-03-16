import json
from zoho_service import get_jobs, create_candidate_application, get_applications


def list_jobs(event, context):

    jobs = get_jobs()

    if "error" in jobs:
        return {
            "statusCode": 500,
            "body": json.dumps(jobs)
        }

    return {
        "statusCode": 200,
        "body": json.dumps(jobs)
    }


def post_candidate(event, context):

    try:

        body = json.loads(event["body"])

        result = create_candidate_application(body)

        if "error" in result:
            return {
                "statusCode": 400,
                "body": json.dumps(result)
            }

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def list_applications(event, context):

    params = event.get("queryStringParameters") or {}

    job_id = params.get("job_id")
    page = int(params.get("page", 1))
    per_page = int(params.get("per_page", 10))

    result = get_applications(job_id, page, per_page)

    if "error" in result:
        return {
            "statusCode": 500,
            "body": json.dumps(result)
        }

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }