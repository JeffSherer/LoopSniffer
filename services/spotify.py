# services/spotify.py

"""
Spotify Search Module for LoopSniffer

This will use the Spotify Web API once client credentials are set up.
"""

def search_remixes(query, limit=25):
    print("[Spotify] Returning mock results.\n")
    return [
        {
            "title": f"{query} (Edit)",
            "artist": "Remix Crew",
            "link": "https://open.spotify.com/track/sample",
            "duration": "4:01"
        }
    ]
