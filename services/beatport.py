from bs4 import BeautifulSoup
from services.base.scraper_base import BaseSniffer
from services.base.scraper_utils import retry_request

class BeatportSniffer(BaseSniffer):
    def search(self):
        query = self.track_name.replace(" ", "+")
        url = f"https://www.beatport.com/search?q={query}"
        response = retry_request(url)

        # Write raw HTML to file for inspection
        with open("beatport_debug.html", "w", encoding="utf-8") as f:
            f.write(response.text)

        print("🧪 Dumped response to beatport_debug.html")
        return self.parse_results(response.text)

    def parse_results(self, html):
        soup = BeautifulSoup(html, "html.parser")

        print("✅ Beatport page loaded")
        links = soup.find_all("a")
        print(f"Found {len(links)} <a> tags")

        matches = []
        for tag in links:
            title = tag.get_text(strip=True)
            if self.match(title):
                print(f"🎯 Match: {title}")
                matches.append(title)

        return matches
