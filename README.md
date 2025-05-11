# LoopSniffer

LoopSniffer is a cross-platform music intelligence tool that sniffs out every remix, edit, bootleg, cover, or alternate version of a song across popular streaming platforms.

It’s designed for DJs, crate diggers, music nerds, and anyone chasing down rare versions of tracks they love.
## Features

- Search multiple streaming platforms with one query
- Detect remix-related tracks based on title patterns (e.g. "remix", "edit", "bootleg")
- Modular design for platform-specific search logic
- Output results to terminal and JSON file
- Scaffolding in place for Spotify, Apple Music, SoundCloud, YouTube Music
## CLI Usage

Run the tool from the root of the project:

python main.py

You’ll be prompted to enter a song name. LoopSniffer will then:

- Search all available services
- Filter for remix-style results
- Print results to terminal
- Save full results to data/<query>_results.json
## Supported Services

| Service        | Status   | Notes                                     |
|----------------|----------|-------------------------------------------|
| YouTube Music  | Ready    | Real API via ytmusicapi                   |
| Apple Music    | Stub     | Will require MusicKit token               |
| Spotify        | Stub     | Will require client credentials           |
| SoundCloud     | Stub     | Planned via scraping or public endpoints  |
## Project Status

The project is in early development. API connections and fuzzy filtering logic will evolve quickly. Contributions and ideas are welcome.
## Project Status

This project is in an early build phase. Initial platform integration, filtering logic, and output formatting are being tested. Development is ongoing.
