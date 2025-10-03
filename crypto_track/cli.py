import argparse
from tabulate import tabulate


currency_symbol_map = {
    "usd": "$",
    "eur": "€",
    "jpy": "¥"
}

def get_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser("Fetch and display real-time cryptocurrency prices.")
    parser.add_argument("cryptocurrencies", nargs="+", action="extend", choices=["bitcoin", "ethereum", "solana"])
    parser.add_argument("-c", "--currency", choices=["eur", "jpy", "usd"], default="usd")

    return parser

def print_table(price_map: dict, target_currency: str) -> None:
    target_currency_symbol = currency_symbol_map.get(target_currency, "")

    headers = ["Cryptocurrency", f"Price ({target_currency.upper()})"]

    table_data = []
    for cryptocurrency, price in sorted(price_map.items()):
        formatted_price = f"{target_currency_symbol}{price:,.2f}"
        table_data.append([cryptocurrency.capitalize(), formatted_price])

    table = tabulate(table_data, headers=headers, tablefmt="grid", colalign=("left", "right"))

    print(table)