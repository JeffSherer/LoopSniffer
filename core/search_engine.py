# core/search_engine.py

from services.apple_music import search_remixes as search_apple
from services.soundcloud import search_remixes as search_soundcloud
from services.spotify import search_remixes as search_spotify
from services.youtube_music import search_remixes as search_youtube

import json
import os

def run_multi_search(query, limit=25):
    all_results = []
    print(f"\n🎧 Sniffing remixes for: {query}\n")

    sources = {
        "Apple Music": search_apple,
        "SoundCloud": search_soundcloud,
        "Spotify": search_spotify,
        "YouTube Music": search_youtube,
    }

    for name, search_fn in sources.items():
        try:
            print(f"🔎 Searching {name}...")
            results = search_fn(query, limit)
            for r in results:
                r["source"] = name
                all_results.append(r)
        except Exception as e:
            print(f"❌ Error searching {name}: {e}")

    # Save results
    os.makedirs("data", exist_ok=True)
    filename = f"data/{query.replace(' ', '_')}_results.json"
    with open(filename, "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"\n📁 Results saved to: {filename}")
    return all_results

