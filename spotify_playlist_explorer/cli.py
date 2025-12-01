# spotify_playlist_explorer/cli.py
from pathlib import Path
import argparse

from spotify_playlist_explorer.pipeline import run_pipeline #, album_pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze a folder of playlist CSVs and produce a master CSV and charts."
    )
    parser.add_argument(
        "input_folder",
        nargs="?",
        help="Path to folder containing CSV files."
            "If omitted, you'll be prompted interactively.",
    )
    parser.add_argument(
        "-o", "--output-folder",
        help="Folder where outputs will be saved (default: ./outputs)",
        default="outputs",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # If user doesn't provide folder as an argument, ask interactively
    if args.input_folder is None:
        input_folder_str = input("Enter the path to the folder with CSVs: ").strip()
    else:
        input_folder_str = args.input_folder

    input_folder = Path(input_folder_str)
    output_folder = Path(args.output_folder)

    if not input_folder.exists() or not input_folder.is_dir():
        print(f"Error: '{input_folder}' is not a valid folder.")
        return

    try:
        master_csv_path = run_pipeline(input_folder, output_folder)
        print("\nAnalysis complete.")
        print(f"- Master CSV: {master_csv_path}")
        print(f"- Outputs folder: {output_folder.resolve()}")
    except Exception as e:
        print(f"Something went wrong: {e}")


    # try:
    #     album_csv_path = album_pipeline(input_folder, output_folder)
    #     print("\nAlbum list complete.")
    #     print(f"- Albums CSV: {album_csv_path}")
    #     print(f"- Outputs folder: {output_folder.resolve()}")
    # except Exception as e:
    #     print(f"Something went wrong with the albums: {e}")
