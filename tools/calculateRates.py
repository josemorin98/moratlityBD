import pandas as pd

def welcome():
    print(f'This is calculae rates')
    
def calculate_crude_rates(dataframe:pd.DataFrame, population:str, count:str) -> pd.DataFrame:
    """
    Calculates rates based on population and count data and adds a new column 'TASA' to the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - population (str): The column name representing the population data.
    - count (str): The column name representing the count data.

    Returns:
    - pd.DataFrame: The DataFrame with the 'TASA' column added, representing the calculated rates.
    """
    dataframe['TASA'] = dataframe[count] / dataframe[population] * 100000
    return dataframe