import requests
import time
from requests.exceptions import RequestException

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

def retry_request(url, max_retries=3, timeout=5):
    for attempt in range(max_retries):
        try:
            res = requests.get(url, headers=HEADERS, timeout=timeout)
            res.raise_for_status()
            return res
        except RequestException:
            time.sleep(1)
    return None
