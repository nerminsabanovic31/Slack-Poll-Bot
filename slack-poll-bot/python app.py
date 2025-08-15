# slack-poll-bot/app.py
import os
import requests

# Slack token i kanal iz environment varijabli
SLACK_TOKEN = os.environ['SLACK_TOKEN']
CHANNEL = "#general"  # ili ime tvog kanala

def send_poll():
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "channel": CHANNEL,
        "text": "Daily poll",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Are you working today?*"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Remote"},
                        "value": "remote"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Home"},
                        "value": "home"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Off - Not working"},
                        "value": "off"
                    }
                ]
            }
        ]
    }

    response = requests.post("https://slack.com/api/chat.postMessage", json=payload, headers=headers)
    print(response.json())

if __name__ == "__main__":
    send_poll()
