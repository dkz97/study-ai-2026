# http api demo
import requests


# Send a request to a public API
rep = requests.get("https://api.coingecko.com/api/v3/ping")
print(str(rep.content))


# Print the JSON response
rep = requests.get("https://api.coingecko.com/api/v3/ping")
print(str(rep.json()))

# Extract select field from the JSON response
rep = requests.get("https://api.coingecko.com/api/v3/ping")
rep_content_json = rep.json()
print(rep_content_json.get("gecko_says"))