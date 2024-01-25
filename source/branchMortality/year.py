import pandas as pd
from tools import handlingData

def generateYear(dataframe:pd.DataFrame, columnsGruops:list, columnCount:str, columnsPopulation:list) -> pd.DataFrame:
    """
    Generates a DataFrame with yearly counts based on specified grouping columns and a count column.

    Parameters:
    - dataframe (DataFrame): The pandas DataFrame to be used for generating yearly counts.
    - columns_groups (list): The columns by which to group the DataFrame.
    - column_count (str): The column for which occurrences will be counted.
    - column_population (list): Thecolumns by which to group the population.

    Returns:
    - df_result (DataFrame): A new DataFrame with yearly counts based on specified grouping columns and count column.
    """
    
    print(f'Group by year')
    
    # Set column cuase with total
    dataframe['CAUSA_DEF'] = 'Total'

    # counting causes by year
    df_result = handlingData.group_by(dataframe=dataframe,
                                       by_columns=columnsGruops,
                                       count_column=columnCount)
    
    # get poblation by nation
    df_result = handlingData.addPoblationNation(dataframe=df_result,
                                                sex=False,
                                                rangeAge=False,
                                                columnsMerge=columnsPopulation)
    
    return df_result