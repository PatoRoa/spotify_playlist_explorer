# analysis/cleaning.py
import pandas as pd


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Apply cleaning steps to the combined Dataframe"""
    df = df.copy()

    # Drop columns
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]

    # Drop missing values
    df.replace("", float("NaN"), inplace=True)
    df = df.dropna(how="any")

    # Restrict to required columns
    required_cols = ["Artist", "Genres", "Album", "Album Date"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"One or more required columns not found.")

    # Clean date strings
    if "Album Date" in df.columns:
        col = "Album Date"
        df[col] = df[col].astype(str)

        # Fix %Y-00-00 to %Y-01-01
        df[col] = df[col].str.replace(r"-00-00$", "-01-01", regex=True)

        # Fix %Y-%M-00 to %Y-%M-01
        df[col] = df[col].str.replace(r"-00$", "-01", regex=True)

        # Fix %Y-%M to %Y-%M-01
        df[col] = df[col].str.replace(r"^(\d{4})-(\d{2})$", r"\1-\2-01", regex=True)

        print(f"[cleaning] df[col]", df[col].head(100))

        df[col] = pd.to_datetime(df[col], errors="coerce")

    return df


def keep_albums(df: pd.DataFrame) -> pd.DataFrame:
    """Apply cleaning steps to the Album Dataframe"""
    df = df.copy()

    # Drop columns
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]

    # Drop missing values
    df.replace("", float("NaN"), inplace=True)
    df = df.dropna(how="any")

    # Restrict to required columns
    required_cols = ["Album", "Artist", "Album Date"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"One or more required columns not found.")

    # Clean Dataframe dates
    col = "Album Date"

    # Fix %Y-00-00 to %Y-01-01
    df[col] = df[col].str.replace(r"-00-00$", "-Unknown", regex=True)

    df = df[["Album", "Artist", "Album Date"]]
    df = df.drop_duplicates()

    return df
