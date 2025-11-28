# spotify_playlist_explorer/pipeline.py
from pathlib import Path

from .analysis.io_utils import load_folder_csvs, save_master_csv
from .analysis.cleaning import clean_dataframe
from .analysis.features import add_features
from .analysis.stats import make_summaries
from .analysis.plots import plot_all


def run_pipeline(input_folder: Path, output_folder: Path) -> Path:
    """
    :param input_folder:
    :param output_folder:
    :return:

    Core pipeline:
    - Read all CSVs in a folder
    - Clean them
    - Add features if needed
    - Compute statistics
    - Make plots
    - Save master CSV

    Returns the path to the master CSV
    """
    output_folder.mkdir(parents=True, exist_ok=True)

    df = load_folder_csvs(input_folder)
    df = clean_dataframe(df)
    df = add_features(df)

    summaries = make_summaries(df)
    plot_all(df, summaries, output_folder)

    master_csv_path = save_master_csv(df, output_folder, name='master.csv')
    return master_csv_path
