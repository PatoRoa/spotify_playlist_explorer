# analysis/stats.py
import pandas as pd


def make_summaries(df: pd.DataFrame) -> dict:
    """
    :param df:
    :return:

    Compute summary tables: counts per year, artist, genre, etc.
    Returns a dictionary of Dataframes to use in plots or prints.
    """
    summaries = {}

    if "year" in df.columns:
        year_counts = (
            df["year"]
            .value_counts()
            .rename_axis("year")
            .reset_index(name="count")
            .sort_values("year")
        )
        summaries["year_counts"] = year_counts
        print(f"[stats] year_counts built, shape={year_counts.shape}")

    else:
        print("[stats] No 'year' column in df; year_counts not built.")

    if "Artist" in df.columns:
        artist_counts = (
            df["Artist"]
            .value_counts()
            .rename_axis("Artist")
            .reset_index(name="count")
        )
        summaries["artist_counts"] = artist_counts
        print(f"[stats] artist_counts built, shape={artist_counts.shape}")

    else:
        print("[stats] No 'Artist' column; artist_counts not built.")

    # TODO: handle Genres

    return summaries