# main.py

from core.search_engine import run_multi_search

def run_cli():
    query = input("🔍 Enter a song name to sniff remixes: ").strip()
    results = run_multi_search(query)

    if not results:
        print("No remix-related results found.")
    else:
        print(f"\n🎛️ Found {len(results)} total remix-style results:\n")
        for track in results:
            print(f"[{track['source']}] {track['title']} by {track['artist']} ({track.get('duration', '??')})")
            print(f"🔗 {track['link']}\n")

if __name__ == "__main__":
    run_cli()
