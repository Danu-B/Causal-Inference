import numpy as np
import pandas as pd

def percent_missing_values(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

def count_missing_rows(df):

    # Calculate total number rows with missing values
    missing_rows = sum([True for idx,row in df.iterrows() if any(row.isna())])

    # Calculate total number of rows
    total_rows = df.shape[0]

    # Calculate the percentage of missing rows
    print(f"{missing_rows} rows({round(((missing_rows/total_rows) * 100), 2)}%) contain atleast one missing value.")

# Function to calculate missing values by column
def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * mis_val / len(df)

    # dtype of missing values
    mis_val_dtype = df.dtypes

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values', 2: 'Dtype'})

    # Sort the table by percentage of missing descending and remove columns with no missing values
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,0] != 0].sort_values(
    '% of Total Values', ascending=False).round(2)

    # Print some summary information
    print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
        "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")

    if mis_val_table_ren_columns.shape[0] == 0:
        return

    # Return the dataframe with missing information
    return mis_val_table_ren_columns

def fix_missing_value(df, cols, value):
    for col in cols:
        count = df[col].isna().sum()
        df[col] = df[col].fillna(value)
        if type(value) == 'str':
            print(f"{count} missing values in the column {col} have been replaced by \'{value}\'.")
        else:
            print(f"{count} missing values in the column {col} have been replaced by {value}.")

def drop_duplicates(df):
    old = df.shape[0]
    df.drop_duplicates(inplace=True)
    new = df.shape[0]
    count = old - new
    if (count == 0):
        print("No duplicate rows were found.")
    else:
        print(f"{count} duplicate rows were found and removed.")

def drop_rows_with_missing_values(df):
    old = df.shape[0]
    df.dropna(inplace=True)
    new = df.shape[0]
    count = old - new
    print(f"{count} rows containg missing values were dropped.")

def drop_columns(df, columns):
    df.drop(columns, axis=1, inplace=True)
    count = len(columns)
    if count == 1:
        print(f"{count} column was dropped.")
    else:
        print(f"{count} columns were dropped.")