import os
import requests
from datetime import datetime
import time

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

# Pokreni bot svakog dana u 07:00 i test danas u 13:00
while True:
    now = datetime.now()
    # Redovni poll u 07:00
    if now.hour == 7 and now.minute == 0:
        send_poll()
        time.sleep(60)
    # Test poll danas u 13:00
    elif now.hour == 13 and now.minute == 0:
        send_poll()
        time.sleep(60)
    time.sleep(20)
