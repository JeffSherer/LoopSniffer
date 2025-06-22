import re
import time
import requests
from requests.exceptions import RequestException

def clean_title(title):
    return re.sub(r"\s+", " ", title.strip().lower())

def match_remix(title):
    lowered = clean_title(title)
    return any(word in lowered for word in ["remix", "edit", "rework", "version"])

def retry_request(url, max_retries=3, timeout=5):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response
        except RequestException as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(1)
def parse_results(self, html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    print("✅ Beatport page loaded")
    print(f"Found {len(soup.find_all('a'))} <a> tags")

    matches = []
    for tag in soup.find_all("a"):
        title = tag.get_text(strip=True)
        if self.match(title):
            print(f"🎯 Match: {title}")
            matches.append(title)
    return matches
