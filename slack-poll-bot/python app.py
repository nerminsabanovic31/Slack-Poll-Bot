import os
import requests

SLACK_TOKEN = os.environ['SLACK_TOKEN']
CHANNEL = "D02GY0HGEFN"  # General channel ID

def send_poll():
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "channel": CHANNEL,
        "text": "Are you working today?",
        "blocks": [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "*Are you working today?*"}
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "🏠 Remote"},
                        "action_id": "remote"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "🏢 Office"},
                        "action_id": "office"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "⛔ Off"},
                        "action_id": "off"
                    }
                ]
            }
        ]
    }

    response = requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=payload)
    print(response.json())

if __name__ == "__main__":
    send_poll()
