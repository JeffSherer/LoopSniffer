from services.adapters import (
    spotify_adapter,
    soundcloud_adapter,
    youtube_adapter,
    beatport_adapter,
    bandcamp_adapter,
    apple_adapter,
    traxsource_adapter,
)

def sniff_all(track_name):
    sniffers = [
        #spotify_adapter,
        soundcloud_adapter,
        #youtube_adapter,
        #beatport_adapter,
        #bandcamp_adapter,
        #apple_adapter,
        #traxsource_adapter,
    ]

    all_results = []
    for module in sniffers:
        print(f"🔍 Running {module.__name__}...")
        try:
            results = module.search(track_name)
            print(f"✅ {module.__name__} returned {len(results)} results")
            all_results.extend(results)
        except Exception as e:
            print(f"❌ {module.__name__} failed: {e}")

    return all_results
