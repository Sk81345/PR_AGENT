import os

import json

import requests
 
def send_slack_notification(message: str):

    url = os.getenv("SLACK_WEBHOOK_URL")
 
    if not url:

        print("SLACK_WEBHOOK_URL is missing")

        return
 
    payload = {"text": message}

    try:

        r = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

        print(" Slack request done")

        print("Slack status:", r.status_code)

        print("Slack response:", r.text)
 
        # If Slack didn't accept, fail the workflow so we know immediately

        if r.status_code != 200 or r.text.strip().lower() != "ok":

            raise Exception(f"Slack webhook failed: {r.status_code} {r.text}")
 
    except Exception as e:

        print(" Slack exception:", str(e))

        raise
 
