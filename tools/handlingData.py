import pandas as pd
import glob
from tools.catalogs import Catalogs
import json
 
catalogsFunctions = Catalogs()
    
def welcome():
    return print("Crated by Morin,JC!")
        
def read_csv_files(files_pattern:list, colums_select:list):
    """
    Reads all CSV files from the specified directory and returns a dictionary
    where keys are file names and values are pandas DataFrames.
        
    Parameters:
    - files_pattern (str): The path of the directory containing CSV files.
    - colums_select (list): A list of column names
    
    Returns:
    - dict: A dictionary where keys are file names and values are DataFrames.
    """
    # Glbal DataFrame
    df_results = pd.DataFrame()
    
    # Get the list of files matching the pattern
    files = glob.glob(files_pattern)

    # For loop to read each file
    for file_path in files:
        # Read the file
        dataFile = pd.read_csv(file_path, low_memory=False)

        # Try to convert all column names to uppercase and select only specific columns.
        try:
            # Convert column names to uppercase.
            dataFile.columns = dataFile.columns.str.upper()
            # Select only the specific columns (previously defined in colums_select) and create a copy.
            dataFile = dataFile[colums_select].copy()    
        # If any exception occurs during the execution of the try block, print a message indicating that the conversion to uppercase couldn't be performed.
        except:
            print('NOT UPPERCASE')
            
        # Print file read
        print(f"Reading file: {file_path}")
        print("=" * 50)  # Divider line for clarity

        df_results = pd.concat([df_results,dataFile])
    
    return df_results

def filter_data_conditions(dataframe: pd.DataFrame, conditions:json):
    """
    Filters a DataFrame using multiple conditions with .loc.

    Parameters:
    - dataframe: DataFrame with data
    - conditions (dict): A dictionary where the keys are the column names
                           and the values are the desired values for those columns.
    Example:
            condition_json = {
                                var1 : [value, condition],
                                var2 : [value, condition]
                            }
        Conditions sign: '<' or '>' or '==' or '<=' or '>=' or '!='
    Returns:
        pd.DataFrame: A new DataFrame containing rows that meet all the conditions.
    """
    filtered = dataframe.copy()
    for column, value in conditions.items():
        if isinstance(value[0], str):
            filtered = filtered.query("{} {} \'{}\'".format(column,value[1],value[0])).copy()
            # print("{} {} \'{}\'".format(column,value[1],value[0]))
        else:
            #print('{} {} {}'.format(column,value[1],value[0]))
            filtered = filtered.query("{} {} {}".format(column,value[1],value[0])).copy()
    return filtered
    
def add_age_by_column(dataframe:pd.DataFrame, columnAge:str):
    edades = catalogsFunctions.get_edad()
    dataframe = dataframe.merge
    