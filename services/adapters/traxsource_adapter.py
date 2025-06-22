from services.base.scraper_base import BaseSniffer

class PlatformSniffer(BaseSniffer):
    def search(self):
        # TODO: implement scraping or API call
        return []

def search(track_name):
    return PlatformSniffer(track_name).search()
