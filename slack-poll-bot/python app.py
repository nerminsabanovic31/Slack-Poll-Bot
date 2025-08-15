import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Koristi varijablu koju već imaš
slack_token = os.environ["SLACK_TOKEN"]
client = WebClient(token=slack_token)

channel_id = "D02GY0HGEFN"

text = "*Are you working today?*\n\n" \
       "🏠 Remote\n" \
       "🏢 Office\n" \
       "🛑 Off - Not working"

try:
    response = client.chat_postMessage(
        channel=channel_id,
        text=text
    )
    
    ts = response["ts"]
    client.reactions_add(channel=channel_id, name="house", timestamp=ts)
    client.reactions_add(channel=channel_id, name="office", timestamp=ts)
    client.reactions_add(channel=channel_id, name="no_entry_sign", timestamp=ts)

    print("Poruka poslata i reakcije dodane!")

except SlackApiError as e:
    print(f"Greška: {e.response['error']}")
