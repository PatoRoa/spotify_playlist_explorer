# analysis/features.py
import pandas as pd


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add derived columns"""
    df = df.copy()

    # Year
    if "Album Date" in df.columns:
        df["Album Date"] = pd.to_datetime(df["Album Date"], errors="coerce")
        df["year"] = df["Album Date"].dt.year

    else:
        print("[features] Warning: 'Album Date' column not found; 'year' will not be created.")
        pass

    # Primary genre
    if "Genres" in df.columns:
        genres = df["Genres"].fillna("").astype(str)
        df["primary_genre_list"] = genres.str.split(',')
        df["primary_genre"] = df["primary_genre_list"].str.get(0).str.strip()

    else:
        pass

    # Parent genre
    if "Parent Genres" in df.columns:
        parent_genres = df["Parent Genres"].fillna("").astype(str)
        df["parent_genre_list"] = parent_genres.str.split(',')
        df["parent_genre"] = df["parent_genre_list"].str.get(0).str.strip()

    else:
        pass

    return df