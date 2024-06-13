"""
Data Filtering Script

This script loads a cleaned CSV file, defines functions to filter data by various criteria, and applies one of the filters to save the filtered data to a new CSV file.

Modules:
    - pandas: Used for data manipulation and analysis.

Functions:
    - filter_by_segment(segment): Filters the data by the specified segment.
    - filter_by_interaction(interaction): Filters the data by the specified interaction.
    - filter_by_activity(activity): Filters the data by the specified activity indicator.

Usage:
    Define the desired filtering criteria and apply the filter. The filtered data will be saved to 'filtered_data.csv'.

"""
import pandas as pd

df = pd.read_csv('cleaned_data.csv')

def filter_by_segment(segment):
    """
    Filters the data by the specified segment.

    Parameters:
        segment (str): The segment to filter by.

    Returns:
        DataFrame: A DataFrame containing rows that match the specified segment.
    """
    return df[df['segment'] == segment]

def filter_by_interaction(interaction):
    """
    Filters the data by the specified interaction.

    Parameters:
        interaction (str): The interaction type to filter by.

    Returns:
        DataFrame: A DataFrame containing rows that match the specified interaction.
    """
    return df[df['interaction'] == interaction]

def filter_by_activity(activity):
    """
    Filters the data by the specified activity indicator.

    Parameters:
        activity (str): The activity indicator to filter by ('active' or 'inactive').

    Returns:
        DataFrame: A DataFrame containing rows that match the specified activity indicator.
    """
    return df[df['active_ind'] == activity]

filtered_data = filter_by_segment('some_segment')
filtered_data.to_csv('filtered_data.csv', index=False)
