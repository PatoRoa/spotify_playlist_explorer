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

    # Year
    if "year" in df.columns:
        year_counts = (
            df["year"]
            .value_counts()
            .rename_axis("year")
            .reset_index(name="count")
            .sort_values("year")
        )
        summaries["year_counts"] = year_counts

    else:
        print("[stats] No 'year' column in df; year_counts not built.")
        pass

    # Artists
    if "Artist" in df.columns:
        def escape_for_plt(s: str) -> str:
            if not isinstance(s, str):
                return s
            return s.replace("$", r"\$")

        artist_counts = (
            df["Artist"]
            .value_counts()
            .rename_axis("Artist")
            .reset_index(name="count")
        )
        summaries["artist_counts"] = artist_counts
        summaries["artist_counts"]["Artist"] = summaries["artist_counts"]["Artist"].map(escape_for_plt)

    else:
        print("[stats] No 'Artist' column; artist_counts not built.")
        pass

    # Genres
    if "primary_genre" in df.columns:
        primary_genre_counts = (
            df["primary_genre"]
            .value_counts()
            .rename_axis("primary_genre")
            .reset_index(name="count")
        )

        summaries["primary_genre_counts"] = primary_genre_counts

    else:
        print("[stats] No 'primary_genre' column in df; primary_genre_counts not built.")
        pass

    if "parent_genre" in df.columns:
        parent_genre_counts = (
            df["parent_genre"]
            .value_counts()
            .rename_axis("parent_genre")
            .reset_index(name="count")
        )

        summaries["parent_genre_counts"] = parent_genre_counts

    else:
        print("[stats] No 'parent_genre' column in df; parent_genre_counts not built.")
        pass

    return summaries