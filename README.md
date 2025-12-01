# Spotify Playlist Explorer
A desktop program for exploring CSV playlist data: merging, cleaning, and creating charts.

## Overview
Spotify Playlist Explorer is a Python application that processes a folder of CSV files that contain Spotify song metadata (e.g., playlists exported with song names, artists, genres, albums, etc.) from Chosic.

The application:
- Loads all CSVs in a folder
- Cleans the data
- Extracts features like album release year and primary and parent genres
- Generates summary statistics
- Creats visualizations based on counts
- Outputs a final master CSV and plot images

It works as a Python CLI program and a standalone Windows .exe for non-programmers.


## Features
- Merge multiple CSVs into a single dataset
- Automatic cleaning:
-   Removes invalid rows
-   Fixes malformed dates
-   Drops unnecessary columns
- Extracts features (year, primary genre, parent genre)
- Summary statistics
-   Most represented years
-   Most frequent artists
-   Most represented genres
- Matplotlib-based charts
- Outputs all results into a clean `outputs/` directory

## Project Structure
```
spotify_playlist_explorer/
├─ spotify_playlist_explorer/
│  ├─ __init__.py
│  ├─ __main__.py
│  ├─ cli.py               # User-facing command-line interface
│  ├─ pipeline.py          # Main processing pipeline
│  ├─ analysis/
│  │  ├─ io_utils.py       # Load/save CSVs and handle output dirs
│  │  ├─ cleaning.py       # Data cleaning and validation
│  │  ├─ features.py       # Extracting columns
│  │  ├─ stats.py          # Summary tables
│  │  └─ plots.py          # Visualizations
├─ run_spotify_playlist_explorer.py   # Entry-point for PyInstaller builds
├─ outputs/                          # Generated at runtime
├─ pyproject.toml
└─ README.md
```

## Running the Program
### Requirements
- Python 3.10+
- Dependencies
-   `pandas`, `matplotlib`

### Usage
1. Create a folder with your CSV playlist files
2. Download `SpotifyPlaylistExplorer_v1.zip` and extract it
3. Double-click the `.exe`
4. When prompted, paste your CSV folder path
5. When complete, the application will create an `outputs/` folder that contains the master CSV and charts
