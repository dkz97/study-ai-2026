import requests
import json

# request a public crypto price api
def req_crypto_price():
    return requests.get("https://api.binance.com/api/v3/ticker/price")



# save JSON data to a local file
def save_json(path, c_json):
    with open(path, "w") as file:
        json.dump(c_json, file, indent=4)



if __name__ == '__main__':
    rep = req_crypto_price()
    save_json("price_json.json", rep.json())