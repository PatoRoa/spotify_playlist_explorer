# spotify_playlist_explorer/analysis/plots.py
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import pandas as pd


fallback_fonts = ["MS Gothic", "Arial Unicode MS", "Noto Sans CJK JP"]
for f in fallback_fonts:
    try:
        plt.rcParams["font.family"] = f
        break
    except:
        pass


def plot_all(df: pd.DataFrame, summaries: dict, output_dir: Path) -> None:
    """Create and save plots. Currently: only year_counts."""

    # Make sure output folder exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get year_counts
    year_counts = summaries.get("year_counts")

    # If summary is missing, build it as a fallback
    if year_counts is None:
        if "year" in df.columns:
            print("[plots] year_counts missing; building from df['year']")
            year_counts = (
                df["year"]
                .value_counts()
                .rename_axis("year")
                .reset_index(name="count")
                .sort_values("year")
            )
        else:
            print("[plots] No 'year' column in df; skipping year plot")
            return

    if year_counts.empty:
        print("[plots] year_counts is empty; no plot will be created")
        return

    print(f"[plots] year_counts shape: {year_counts.shape}")
    print(f"[plots] first few rows:\n{year_counts.head()}")

    # Song counts bar plot
    # Bar plot colors
    counts = year_counts["count"].values
    norm = colors.Normalize(vmin=counts.min(), vmax=counts.max())
    cmap = cm.get_cmap("viridis")

    # Bar plot
    plt.figure(figsize=(14, 7))
    plt.bar(year_counts["year"], year_counts["count"], color=cmap(norm(counts)))
    plt.xticks(ticks=year_counts["year"], rotation=90)
    plt.title("Songs by Year")
    plt.tight_layout()

    out_path = output_dir / "year_counts.png"
    plt.savefig(out_path)
    plt.close()

    print(f"[plots] Saved year_counts.png to: {out_path.resolve()}")


    # Get artist counts
    artist_counts = summaries.get("artist_counts")

    # If summary is missing, build it as a fallback
    if artist_counts is None:
        if "Artist" in df.columns:
            print("[plots] artist_counts missing; building from df['Artist']")
            artist_counts = (
                df["Artist"]
                .value_counts()
                .rename_axis("Artist")
                .reset_index(name="count")
                .sort_values("Artist")
            )
        else:
            print("[plots] No 'Artist' column in df; skipping year plot")
            return

    if artist_counts.empty:
        print("[plots] artist_counts is empty; no plot will be created")
        return

    print(f"[plots] artist_counts shape: {artist_counts.shape}")
    print(f"[plots] first few rows:\n{artist_counts.head()}")

    # Artist counts bar plot
    artist_counts_top = artist_counts.head(30)

    # Bar plot colors
    counts = artist_counts_top["count"].values
    norm = colors.Normalize(vmin=counts.min(), vmax=counts.max())
    cmap = cm.get_cmap("plasma")

    # Bar plot
    plt.figure(figsize=(14, 7))
    plt.bar(artist_counts_top["Artist"], artist_counts_top["count"], color=cmap(norm(counts)))
    plt.xticks(rotation=90)
    plt.title("Top 30 Artists by Representation")
    plt.tight_layout()

    out_path = output_dir / "artist_counts.png"
    plt.savefig(out_path)
    plt.close()

    print(f"[plots] Saved year_counts.png to: {out_path.resolve()}")

    # Get genre counts
    primary_genre_counts = summaries.get("primary_genre_counts")

    if primary_genre_counts.empty:
        print("[plots] primary_genre_counts is empty; no plot will be created")
        return

    # Genre counts bar plot
    primary_genre_top = primary_genre_counts.head(10)

    print(f"[plots] primary_genre_counts shape: {primary_genre_top.shape}")
    print(f"[plots] first few rows:\n{primary_genre_top.head()}")

    # Bar plot colors
    counts = primary_genre_top["count"].values
    norm = colors.Normalize(vmin=counts.min(), vmax=counts.max())
    cmap = cm.get_cmap("inferno")

    # Bar plot
    plt.figure(figsize=(14, 7))
    plt.bar(primary_genre_top["primary_genre"], primary_genre_top["count"], color=cmap(norm(counts)))
    plt.xticks(rotation=90)
    plt.title("Top 10 Primary Genres by Representation")
    plt.tight_layout()

    out_path = output_dir / "primary_genre_counts.png"
    plt.savefig(out_path)
    plt.close()

    print(f"[plots] Saved primary_genre_counts.png to: {out_path.resolve()}")

    # Get parent genre counts
    parent_genre_counts = summaries.get("parent_genre_counts")

    if parent_genre_counts.empty:
        print("[plots] parent_genre_counts is empty; no plot will be created")
        return

    # Genre counts bar plot
    parent_genre_top = parent_genre_counts.head(10)

    print(f"[plots] parent_genre_top shape: {parent_genre_top.shape}")
    print(f"[plots] first few rows:\n{parent_genre_top.head()}")

    # Bar plot colors
    counts = parent_genre_top["count"].values
    norm = colors.Normalize(vmin=counts.min(), vmax=counts.max())
    cmap = cm.get_cmap("viridis")

    # Bar plot
    plt.figure(figsize=(14, 7))
    plt.bar(parent_genre_top["parent_genre"], parent_genre_top["count"], color=cmap(norm(counts)))
    plt.xticks(rotation=90)
    plt.title("Top 10 Parent Genres by Representation")
    plt.tight_layout()

    out_path = output_dir / "parent_genre_counts.png"
    plt.savefig(out_path)
    plt.close()

    print(f"[plots] Saved parent_genre_counts.png to: {out_path.resolve()}")