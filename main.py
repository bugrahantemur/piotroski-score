import pandas as pd
from fscore import f_score

if __name__ == "__main__":
    # Read the data as csv and create a pandas DataFrame
    data = pd.read_csv("./data/fundamentals.csv", index_col=0)

    # Set the year of calculation for Piotroski F-Score
    year = 2022

    # Get new field "F-Score"
    data["F-Score"] = f_score(data, year)

    # Print the "F-Score" column to the console
    print(data.to_string(columns=["F-Score"]))
