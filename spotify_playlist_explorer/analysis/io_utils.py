# spotify_playlist_explorer/analysis/io_utils.py
from pathlib import Path
import pandas as pd


def load_folder_csvs(folder: Path) -> pd.DataFrame:
    """Load all CSVs in the folder and concatenate them into one Dataframe."""
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Provided path is not a directory: {folder}")

    csv_files = list(folder.glob("*.csv"))
    if not csv_files:
        raise ValueError(f"No CSV files found in {folder}")

    dfs = []
    for file in csv_files:
        df = pd.read_csv(file)
        dfs.append(df)

    combined = pd.concat(dfs, ignore_index=True)
    return combined


def save_master_csv(df: pd.DataFrame, output_dir: Path, name: str) -> Path:
    """Save the combined Dataframe as master CSV."""
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / name
    df.to_csv(out_path, index=False)
    return out_path