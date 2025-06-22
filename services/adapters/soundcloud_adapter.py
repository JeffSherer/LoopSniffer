from services.base.scraper_base import BaseSniffer
import requests

class SoundCloudSniffer(BaseSniffer):
    def __init__(self, track_name):
        super().__init__(track_name)
        self.client_id = "HcZ8JYqXbktptcJG5UMnF2cBDu5Hh5kU"  # public key

    def search(self):
        url = "https://api-v2.soundcloud.com/search/tracks"
        params = {
            "q": self.track_name,
            "client_id": self.client_id,
            "limit": 20
        }
        print("📡 Requesting SoundCloud with params:", params)
        res = requests.get(url, params=params)
        print("📥 Status code:", res.status_code)
        res.raise_for_status()
        data = res.json()

        results = []
        for item in data.get("collection", []):
            results.append({
                "platform": "SoundCloud",
                "title": item["title"],
                "artist": item["user"]["username"],
                "link": item["permalink_url"],
                "duration": f"{item['duration'] // 1000}s"
            })
        print("🎯 Total results:", len(results))
        return results

def search(track_name):
    return SoundCloudSniffer(track_name).search()
