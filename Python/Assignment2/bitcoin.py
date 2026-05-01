import sys
import requests


def main():
    # Checkcommand-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")


    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Command-line argument must be a number")

    #CoinCap API to certain Bitcoin price
    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        response.raise_for_status()
        data = response.json()

        # Extract the current Bitcoin price from the nested JSON
        bitcoin_price = float(data["data"]["priceUsd"])

    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price from API")
    except (KeyError, ValueError):
        sys.exit("Error: Unable to parse Bitcoin price from API response")


    total_cost = n * bitcoin_price


    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
