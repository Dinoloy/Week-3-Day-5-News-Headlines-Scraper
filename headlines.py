import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0.0.0 Safari/537.36"
}

try:
    response = requests.get(URL, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract BBC headline elements
    items = soup.select("h2[data-testid='card-headline']")

    if not items:
        items = soup.select("h2")

    headlines = []
    seen = set()

    for item in items:
        headline = item.get_text(" ", strip=True)

        if headline and headline not in seen:
            headlines.append(headline)
            seen.add(headline)

        if len(headlines) == 5:
            break

    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")

    if len(headlines) < 5:
        print(f"Only {len(headlines)} unique headlines found.")

except requests.RequestException as error:
    print(f"Error fetching news: {error}")