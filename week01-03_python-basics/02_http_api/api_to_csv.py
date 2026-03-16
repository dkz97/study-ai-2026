import requests
import csv

# Request crypto price data from binance public API
def req_crypto_price():
    return requests.get("https://api.binance.com/api/v3/ticker/price")


# Extract symbol and file from json and save them to a local CSV file
def to_csv(file_path, rep):
    json_data = rep.json()
    # use open() function get file object
    with open(file_path, "w", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, ['symbol','price'])
        csv_writer.writeheader()
        csv_writer.writerows(json_data)


if __name__ == '__main__':
    rep = req_crypto_price()
    # Raise an exception if the request fails
    rep.raise_for_status()
    to_csv('price.csv', rep)
