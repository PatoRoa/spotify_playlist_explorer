# cleaner.py
import glob
import pandas as pd
from pathlib import Path


def one_folder_up(path: str):
    # Saves user-given path as Path
    p = Path(path)

    # Goes up one directory and creates new clean folder
    parent_dir = p.parent
    new_folder = parent_dir / (p.name + "_clean")
    new_folder.mkdir(exist_ok=True)

    print(f"New folder created: {new_folder}")
    return new_folder


def cleaner(path: str):
    p = Path(path)
    clean_folder = p.parent / (p.name + "_clean")

    # New folder for clean CSV files
    new_dir = one_folder_up(path)

    if not clean_folder.exists() or not any(clean_folder.iterdir()):
        print("Inside if statement reached")

        # Take all CSV files
        files = glob.glob(path + "/*.csv")

        for file in files:
            # Put CSV into dataframe
            df = pd.read_csv(file)

            # Keep necessary columns
            df_clean = df[["#", "Song", "Artist", "Genres", "Album", "Album Date"]].set_index("#")

            # Change date column to Date

            # Change apparent %Y-00-00 dates to %Y-01-01
            # Fix YYYY-00-00
            df_clean["Album Date"] = df_clean["Album Date"].str.replace(r"-00-00$", "-01-01", regex=True)
            # Fix YYYY-MM-00
            df_clean["Album Date"] = df_clean["Album Date"].str.replace(r"-([0-9]{2})-00$", r"-\1-01", regex=True)
            # Fix YYYY-MM-01
            df_clean["Album Date"] = df_clean["Album Date"].str.replace(r"^(\d{4})-(\d{2})$", r"\1-\2-01", regex=True)

            # Drop duplicate rows
            df_clean = df_clean.dropna()
            df_clean = df_clean.drop_duplicates()

            # Clean CSV naming
            print(f"Type a new name for the file '{Path(file).name}'.")
            new_name = input()
            new_name = new_name + "_clean"
            new_path = str(new_dir) + "/" + new_name + ".csv"

            df_clean.to_csv(new_path)

            print(f"New CSV {new_name + '.csv'} saved to {new_path}.\n")

        # New CSV for albums and artists
        df_albums = df_clean[["Album", "Artist", "Album Date"]]
        df_albums_path = str(new_dir) + "/albums" + ".csv"
        df_albums.to_csv(df_albums_path)

        print(f"New CSV albums.csv saved to {df_albums_path}.\n")

    else:
        pass

    return new_dir
