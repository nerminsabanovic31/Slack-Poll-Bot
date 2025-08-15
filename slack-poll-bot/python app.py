import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Token bota (dodaj ga u Secrets GitHub-a kao SLACK_BOT_TOKEN)
slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)

# ID kanala #general
channel_id = "D02GY0HGEFN"

# Poruka
text = "*Are you working today?*\n\n" \
       "🏠 Remote\n" \
       "🏢 Office\n" \
       "🛑 Off - Not working"

try:
    # Pošalji poruku
    response = client.chat_postMessage(
        channel=channel_id,
        text=text
    )
    
    # Dodaj reakcije automatski
    ts = response["ts"]  # timestamp poruke
    client.reactions_add(channel=channel_id, name="house", timestamp=ts)
    client.reactions_add(channel=channel_id, name="office", timestamp=ts)  # možeš zamijeniti sa drugim emoji
    client.reactions_add(channel=channel_id, name="no_entry_sign", timestamp=ts)

    print("Poruka poslata i reakcije dodane!")

except SlackApiError as e:
    print(f"Greška: {e.response['error']}")
