# slack-poll-bot/app.py
import os
import requests

# Slack token i kanal iz environment varijabli
SLACK_TOKEN = os.environ['SLACK_TOKEN']
CHANNEL = "#general"  # ili #tvoj-kanal

def send_poll():
    text = '/poll "Are you working today?" "Remote" "Home" "Off - Not working"'
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "channel": CHANNEL,
        "text": text
    }
    response = requests.post("https://slack.com/api/chat.postMessage", json=payload, headers=headers)
    print(response.json())

if __name__ == "__main__":
    send_poll()
