from services.sniff_controller import sniff_all

if __name__ == "__main__":
    track = "Midnight City"
    results = sniff_all(track)

    for r in results:
        print(f"[{r['platform']}] {r['title']} by {r['artist']}")
        print(f"🔗 {r['link']} ({r['duration']})\n")
