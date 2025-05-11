# services/soundcloud.py

"""
SoundCloud Search Module for LoopSniffer

Eventually will use scraping or unofficial API endpoints. Stub for now.
"""

def search_remixes(query, limit=25):
    print("[SoundCloud] Returning mock results.\n")
    return [
        {
            "title": f"{query} (Bootleg)",
            "artist": "Unknown DJ",
            "link": "https://soundcloud.com/sample",
            "duration": "5:12"
        }
    ]
