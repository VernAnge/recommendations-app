"""
Data Cleaning Script

This script loads a CSV file, performs data cleaning operations, and saves the cleaned data to a new CSV file. The cleaning operations include filling missing values, converting text to lowercase and stripping whitespace, and removing duplicate entries.

Modules:
    - pandas: Used for data manipulation and analysis.

Functions:
    - None

Usage:
    Run the script and it will load the data, perform the cleaning operations, and save the cleaned data to 'cleaned_data.csv'.

"""
import pandas as pd

df = pd.read_csv('data.csv') # Rename to the name of your file
df.fillna('', inplace=True)
df['item_type'] = df['item_type'].str.lower().str.strip()
df['item_descrip'] = df['item_descrip'].str.lower().str.strip()
df['active_ind'] = df['active_ind'].str.lower().str.strip()

df.drop_duplicates(inplace=True)
df.to_csv('cleaned_data.csv', index=False)
