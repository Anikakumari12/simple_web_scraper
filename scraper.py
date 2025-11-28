import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}
BASE_URL = "https://books.toscrape.com/"


def fetch_page(url, timeout=10):
    """
    Download the HTML of `url`.
    - url: full URL to fetch
    - timeout: how long to wait for the server response (seconds)
    Returns the response text (HTML) on success.
    Raises requests.HTTPError on bad status codes.
    """
    response = requests.get(url, headers=HEADERS, timeout=timeout)
    response.raise_for_status()
    return response.text


def parse_books(html):
    """
    Parse the HTML of a books.toscrape.com page and return a list of
    dicts with keys: 'title' and 'price'.
    """
    soup = BeautifulSoup(html, "html.parser")
    results = []

    # each book is inside <article class="product_pod">
    items = soup.find_all("article", class_="product_pod")

    for item in items:
        # title: the <a> tag inside <h3> has the 'title' attribute
        title_tag = item.h3.a
        title = title_tag.get("title", "").strip()

        # price: inside <p class="price_color">£51.77</p>
        price_tag = item.find("p", class_="price_color")
        price_text = price_tag.get_text(strip=True) if price_tag else ""
        # remove currency symbol and convert to float where possible
        price = None
        if price_text:
            # price_text usually like '£51.77' -> strip non-digit characters
            cleaned = price_text.replace("£", "").replace("Â", "")
            try:
                price = float(cleaned)
            except ValueError:
                price = None

        results.append({"title": title, "price": price})

    return results


def save_to_csv(records, output_path="output.csv"):
    """
    Save a list of dicts to CSV using pandas.
    - records: list of dictionaries (each dict is a row)
    - output_path: file path to write CSV
    """
    df = pd.DataFrame(records)
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Saved {len(records)} records to {output_path}")


def main():
    """
    Main orchestration:
    1. fetch page
    2. parse books
    3. save to CSV
    """
    url = BASE_URL  # first page
    print(f"Fetching: {url}")
    html = fetch_page(url)

    print("Parsing books...")
    books = parse_books(html)

    print("Saving results...")
    save_to_csv(books)


if __name__ == "__main__":
    main()
