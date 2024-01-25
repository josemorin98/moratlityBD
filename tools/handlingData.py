import pandas as pd
import glob
from tools.catalogs import Catalogs
import json
from progressbar import ProgressBar
 
catalogsFunctions = Catalogs()
    
def welcome():
    return print("Crated by Morin,JC!")
        
def read_csv_files(files_pattern:list, colums_select:list) -> pd.DataFrame:
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
    with ProgressBar(max_value=len(files)) as bar:
        i=0
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
            # print(f"Reading file: {file_path}")
            # print("=" * 50)  # Divider line for clarity

            df_results = pd.concat([df_results,dataFile])
            del dataFile
            i +=  1
            bar.update(i)
    del files
    
    return df_results

def filter_data_conditions(dataframe: pd.DataFrame, conditions:dict) -> pd.DataFrame:
    """
    Filters a DataFrame using multiple conditions with .loc.

    Parameters:
    - dataframe (Dataframe): DataFrame with data
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
    # Glbal DataFrame
    filtered = dataframe.copy()
    
    # Get items by conditios
    for column, value in conditions.items():
        
        # If value is string then add '' to the query string
        if isinstance(value[0], str):
            filtered = filtered.query("{} {} \'{}\'".format(column,value[1],value[0])).copy()
        
        # If value is not string then not add '' to the query string
        else:
            filtered = filtered.query("{} {} {}".format(column,value[1],value[0])).copy()
    
    return filtered
    
def add_age_by_column(dataframe: pd.DataFrame, columnAge: str) -> pd.DataFrame:
    """
    Adds age information to a DataFrame based on a specified column.

    Parameters:
    - dataframe (pd.DataFrame): The pandas DataFrame to which age information will be added.
    - column_age (str): The name of the column in the DataFrame containing age-related codes.

    Returns:
    - pd.DataFrame: The modified DataFrame with additional age information.
    """
    # Get age information DataFrame
    df_age = catalogsFunctions.get_edad()
    
    # Merge age information with the original DataFrame
    dataframe = dataframe.merge(df_age, left_on=columnAge, right_on='CVE', how='inner')

    # Drop unnecessary columns
    dataframe = dataframe.drop(['EDAD', 'CVE', 'DESCRIP'], axis=1)

    # Release memory by deleting the temporary DataFrame
    del df_age

    return dataframe

def sex_replace(dataframe:pd.DataFrame, sex_column:str) -> pd.DataFrame:
    """
    Replaces numerical gender values with corresponding labels in a DataFrame.

    Parameters:
    - df (DataFrame): The pandas DataFrame containing the data.
    - sex_column (str): The name of the column representing gender with numerical values.

    Returns:
    - DataFrame: The DataFrame with the gender column values replaced.
    """
    # Remplace id sex
    dataframe[sex_column] = dataframe[sex_column].replace({1: 'Hombre', 2: 'Mujer'})
    
    return dataframe

def group_by(dataframe:pd.DataFrame, by_columns:list, count_column:str) -> pd.DataFrame:
    """
    Groups a DataFrame by specified columns and counts occurrences in a specified column.

    Parameters:
    - dataframe (Dataframe): The pandas DataFrame to be grouped.
    - by_columns (list): The columns by which to group the DataFrame.
    - count_column (string): The column for which occurrences will be counted.

    Returns:
    - df_results: A new DataFrame with grouping by specified columns and count information.
    """
    # Group by columns
    dataframe = dataframe.groupby(by=by_columns)[count_column].count().reset_index()
    
    return dataframe

