import os

import json

import urllib.request

import urllib.parse

TOKEN = os.environ["TELEGRAM_TOKEN"]

CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://shop.travisscott.com/products.json?limit=250"

def main():

    req = urllib.request.Request(

        URL,

        headers={"User-Agent": "Mozilla/5.0"}

    )

    with urllib.request.urlopen(req, timeout=20) as response:

        products = json.loads(response.read())

    for product in products.get("products", []):

        title = product.get("title", "")

        if "air force 1" not in title.lower() or "gta" not in title.lower():

            continue

        for variant in product.get("variants", []):

            if variant.get("available"):

                message = (

                    "🔥 AIR FORCE 1 GTA DISPONIBILI!\n"

                    + title + "\n"

                    + str(variant.get("price")) + "\n"

                    + "https://shop.travisscott.com/products/"

                    + product.get("handle", "")

                )

                data = urllib.parse.urlencode({

                    "chat_id": CHAT_ID,

                    "text": message

                }).encode()

                telegram_url = (

                    f"https://api.telegram.org/bot{TOKEN}/sendMessage"

                )

                urllib.request.urlopen(

                    telegram_url, data=data, timeout=20

                )

if __name__ == "__main__":

    main()
