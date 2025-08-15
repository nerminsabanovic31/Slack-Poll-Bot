# slack-poll-bot/app.py
import os
import requests

# Slack token iz GitHub Secrets
SLACK_TOKEN = os.environ['SLACK_TOKEN']

# Tvoj Slack User ID (da poruka ide direktno tebi)
USER_ID = "D02GY0HGEFN"  

def send_poll():
    # Poll komanda koja se šalje
    text = '/poll "Are you working today?" "Remote" "Home" "Off - Not working"'

    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "channel": USER_ID,
        "text": text
    }

    response = requests.post("https://slack.com/api/chat.postMessage", json=payload, headers=headers)
    print(response.json())

if __name__ == "__main__":
    send_poll()

if __name__ == "__main__":
    send_poll()
