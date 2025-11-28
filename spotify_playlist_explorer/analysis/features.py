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

    # TODO: fix 'year' being a float

    # TODO: add features
    # Artist names
    # Artist origins
    # Primary genre

    return df