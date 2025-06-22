from services.adapters import soundcloud_adapter

print("✅ Imported adapter")

results = soundcloud_adapter.search("Midnight City")
print(f"✅ Got {len(results)} results")
for r in results:
    print(f"{r['title']} by {r['artist']} — {r['link']}")

