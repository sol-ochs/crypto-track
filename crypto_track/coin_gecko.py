from json import JSONDecodeError

import requests


class CoinGeckoClient:
    def __init__(self):
        self.url = "https://api.coingecko.com/api/v3/simple/price"

    def fetch_cryptocurrency_data(self, cryptocurrencies: list[str], target_currency: str) -> dict | None:
        try:
            payload = {
                "ids": ",".join(cryptocurrencies),
                "vs_currencies": target_currency
            }

            response = requests.get(self.url, params=payload)

            parsed_response = response.json()

            price_map = {}
            for cryptocurrency, price in parsed_response.items():
                price_map[cryptocurrency] = parsed_response.get(cryptocurrency).get(target_currency)

            return price_map
        except JSONDecodeError as e:
            print(f"Error decoding response: {e}")
        except Exception as e:
            print(f"Error fetching prices: {e}")