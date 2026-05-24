import requests
from bs4 import BeautifulSoup

from shoppinglist.models import Product


def scrape_walmart():

    url = "https://www.walmart.ca/search?q=fruits"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)

    print("STATUS:", response.status_code)

    soup = BeautifulSoup(response.text, "lxml")

    products = soup.find_all(
        "span",
        attrs={"data-automation": "product-title"}
    )

    count = 0

    for item in products:

        name = item.get_text(strip=True)

        if name:

            print(name)

            Product.objects.update_or_create(
                name=name,
                store="Walmart",
                defaults={
                    "category": "Fruits",
                    "price": 0,
                }
            )

            count += 1

    print(f"{count} products saved.")