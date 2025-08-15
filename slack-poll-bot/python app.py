# slack-poll-bot/app.py
import os
import requests
import json

SLACK_TOKEN = os.environ['SLACK_TOKEN']
CHANNEL_ID = "D02GY0HGEFN"  # general kanal

def send_poll():
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "channel": CHANNEL_ID,
        "text": "Are you working today?",
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
                        "text": {"type": "plain_text", "text": "🏠 Remote"},
                        "value": "remote",
                        "action_id": "remote_click"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "🏢 Office"},
                        "value": "office",
                        "action_id": "office_click"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "🛑 Off - Not working"},
                        "value": "off",
                        "action_id": "off_click"
                    }
                ]
            }
        ]
    }

    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers=headers,
        data=json.dumps(payload)
    )
    print(response.json())

if __name__ == "__main__":
    send_poll()
