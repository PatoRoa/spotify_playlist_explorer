# spotify_playlist_explorer/analysis/plots.py

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def plot_all(df: pd.DataFrame, summaries: dict, output_dir: Path) -> None:
    """Create and save plots. Currently: only year_counts."""

    # Make sure output folder exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get year_counts
    year_counts = summaries.get("year_counts")

    # If summary missing, try to build it from df as a fallback
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

    # Simple bar plot with pure matplotlib (no seaborn) ---
    plt.figure(figsize=(10, 5))
    plt.bar(year_counts["year"], year_counts["count"])
    plt.xticks(rotation=90)
    plt.title("Songs by Year")
    plt.tight_layout()

    out_path = output_dir / "year_counts.png"
    plt.savefig(out_path)
    plt.close()

    print(f"[plots] Saved year_counts.png to: {out_path}")
