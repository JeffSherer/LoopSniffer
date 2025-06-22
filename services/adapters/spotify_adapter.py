import os
import requests
from services.base.scraper_base import BaseSniffer

class SpotifySniffer(BaseSniffer):
    def __init__(self, track_name):
        super().__init__(track_name)
        self.token = self.get_token()

    def get_token(self):
        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        auth_url = "https://accounts.spotify.com/api/token"
        response = requests.post(
            auth_url,
            data={"grant_type": "client_credentials"},
            auth=(client_id, client_secret),
        )
        response.raise_for_status()
        return response.json()["access_token"]

    def search(self):
        search_url = "https://api.spotify.com/v1/search"
        params = {"q": self.track_name, "type": "track", "limit": 20}
        headers = {"Authorization": f"Bearer {self.token}"}
        res = requests.get(search_url, headers=headers, params=params)
        res.raise_for_status()
        data = res.json()

        results = []
        for item in data.get("tracks", {}).get("items", []):
            title = item["name"]
            artist = ", ".join([a["name"] for a in item["artists"]])
            link = item["external_urls"]["spotify"]
            duration = item["duration_ms"] // 1000
            results.append({
                "platform": "Spotify",
                "title": title,
                "artist": artist,
                "link": link,
                "duration": f"{duration}s"
            })
        return results

def search(track_name):
    return SpotifySniffer(track_name).search()
