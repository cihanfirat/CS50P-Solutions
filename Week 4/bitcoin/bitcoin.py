import sys
import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

elif len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a valid number")
    else:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=2d2446b35e027203be0aaa174536e036dc8039c2f136d17f884f87360109f4a0")
        o = response.json()
        result = o["data"]
        price = result["priceUsd"]
        finalPrice =float(price)*value
        print(f"${finalPrice:,.4f}")


