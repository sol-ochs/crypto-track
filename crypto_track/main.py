import sys

from crypto_track.coin_gecko import CoinGeckoClient
from crypto_track.cli import get_argument_parser, print_table


def main():
    parser = get_argument_parser()
    args = parser.parse_args()

    cryptocurrencies = args.cryptocurrencies
    target_currency = args.currency

    client = CoinGeckoClient()
    price_map = client.fetch_cryptocurrency_data(cryptocurrencies, target_currency)

    if price_map is None:
        print("Could not retrieve cryptocurrency price(s). Exiting.")
        sys.exit(1)

    print_table(price_map, target_currency)


if __name__ == "__main__":
    main()