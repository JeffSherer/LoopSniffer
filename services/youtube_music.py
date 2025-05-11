# services/youtube_music.py

# Requires: pip install ytmusicapi
from ytmusicapi import YTMusic

yt = YTMusic()

REMIX_KEYWORDS = [
    "remix", "edit", "bootleg", "flip", "rework",
    "version", "mashup", "cover", "live", "extended"
]

def search_remixes(query, limit=25):
    results = yt.search(query, filter="songs", limit=limit)
    remixes = []

    for track in results:
        title = track.get("title", "").lower()
        if any(keyword in title for keyword in REMIX_KEYWORDS):
            remixes.append({
                "title": track.get("title"),
                "artist": track.get("artists", [{}])[0].get("name", "Unknown"),
                "link": f"https://music.youtube.com/watch?v={track.get('videoId')}",
                "duration": track.get("duration", ""),
            })

    return remixes
