"""
Bootstrap Sampling Script

This script loads a cleaned CSV file, generates bootstrap samples to increase the dataset size, and saves the bootstrap samples to a new CSV file. The bootstrap sampling method involves resampling with replacement to create a larger dataset.

Modules:
    - pandas: Used for data manipulation and analysis.
    - numpy: Used for numerical operations.

Functions:
    - create_bootstrap_samples(data, total_samples): Generates bootstrap samples to increase the dataset size.

Usage:
    The script will generate bootstrap samples of twice the size of the original dataset and save the results to 'bootstrap.csv'.

"""
import pandas as pd
import numpy as np

input_file = 'cleaned_data.csv'
data = pd.read_csv(input_file)

def create_bootstrap_samples(data, total_samples):
    """
    Generates bootstrap samples to increase the dataset size.

    Parameters:
        data (DataFrame): The original data to sample from.
        total_samples (int): The total number of samples desired.

    Returns:
        DataFrame: A DataFrame containing the bootstrap samples.
    """
    n = len(data)
    multiplier = total_samples // n
    remainder = total_samples % n
    bootstrap_samples = [data.sample(n, replace=True) for _ in range(multiplier)]
    
    if remainder > 0:
        bootstrap_samples.append(data.sample(remainder, replace=True))
    
    return pd.concat(bootstrap_samples, ignore_index=True)

total_samples = 2 * len(data)
bootstrap_data = create_bootstrap_samples(data, total_samples)
output_file = 'bootstrap.csv'
bootstrap_data.to_csv(output_file, index=False)

print(f"Bootstrap samples saved to {output_file}")
