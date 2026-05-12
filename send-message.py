import os
import requests

webhook_url = os.environ["DISCORD_WEBHOOK_URL"]

message = "$SPY"

response = requests.post(
    webhook_url,
    json={"content": message}
)

response.raise_for_status()