# slack-poll-bot/app.py
import os
import requests

# Slack token iz environment varijabli
SLACK_TOKEN = os.environ['SLACK_TOKEN']

# ID kanala za DM direktno tebi
CHANNEL = "D02GY0HGEFN"

def send_poll():
    # Ovo je samo tekst polla; /poll komanda radi samo u Slack aplikacijama koje imaju Pollys/Slack Slash komande
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
