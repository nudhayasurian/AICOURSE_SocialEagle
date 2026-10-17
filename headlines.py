
import requests
from bs4 import BeautifulSoup

# BBC News URL
url = "https://www.bbc.com/news"

# Browser User-Agent
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    # Fetch BBC News webpage
    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    # Check HTTP response status
    response.raise_for_status()

    print("HTTP Status:", response.status_code)

    # Parse HTML
    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # Extract headlines using inspected selector
    elements = soup.select(
        'h2[data-testid="card-headline"]'
    )

    print("Headlines found:", len(elements))

    # Clean, deduplicate and print headlines
    seen = set()
    headlines = []

    for element in elements:
        headline = element.get_text(
            " ", strip=True
        )

        if not headline:
            continue

        if headline.casefold() in seen:
            continue

        seen.add(headline.casefold())
        headlines.append(headline)

        if len(headlines) == 5:
            break

    for index, headline in enumerate(headlines, 1):
        print(f"{index}. {headline}")

    if len(headlines) < 5:
        print(
            f"Only {len(headlines)} "
            "unique headlines available."
        )

except requests.exceptions.RequestException as error:
    print("Error fetching BBC News:", error)
