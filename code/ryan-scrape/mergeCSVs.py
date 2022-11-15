import os

import pandas as pd


# Merge all csvs in folder into one dataframe
def mergeCSVs(folder):
    # Get all csv files in folder
    csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    # Create dataframe from first csv file
    df = pd.read_csv(folder + csv_files[0])
    # Append dataframes from other csv files
    for csv in csv_files[1:]:
        df = df.append(pd.read_csv(folder + csv))
    return df

mergedCSV = mergeCSVs('data/')

mergedCSV.to_csv('data/dwi.csv', index=False)
