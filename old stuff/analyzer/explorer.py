# explorer.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 1000)


def explorer(path):
    files = list(path.glob("*.csv"))

    df_list = [pd.read_csv(file) for file in files]

    df = pd.concat(df_list)

    # Barplot for Years represented in the dataset
    df["Album Date"] = pd.to_datetime(df["Album Date"])
    df["year"] = df["Album Date"].dt.year

    df_year = df["year"].value_counts().reset_index()

    sns.set(rc={"figure.figsize": (12, 6)})
    bar = sns.barplot(data=df_year, x="year", y='count')
    bar.tick_params(axis='x', labelrotation=90)
    plt.show()

    # Barplot for Genres represented in the dataset
    # print(df.head(100))