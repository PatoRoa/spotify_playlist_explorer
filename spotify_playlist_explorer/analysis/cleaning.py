# analysis/cleaning.py
import pandas as pd


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Apply cleaning steps to the combined Dataframe"""
    df = df.copy()

    # Drop columns
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]

    # TODO: optionally restrict to required columns:

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

        df[col] = pd.to_datetime(df[col], errors="coerce")

    # TODO: handle missing values
    # Missing values
    # Fill null values

    return df
