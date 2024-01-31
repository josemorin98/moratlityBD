import pandas as pd
from source.combinationsMortality import calculateBasic
from progressbar import ProgressBar


def calculateGeneralMortality(dataframe:pd.DataFrame, conditionsGeneral:dict) -> pd.DataFrame:
    """
    Function to calculate differents combinations of data to calculate rates of National.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing the data.
    - conditionsGeneral (dict): A dictionary containing parameters for generating national data combinations.

    Returns:
    - DataFrame: A DataFrame with different combinations of data for rate calculation.
    """
    
    #  Global Dataframe
    df_results = pd.DataFrame()
    
    # Set column count
    conteo = conditionsGeneral['columnCount']
    dataframe['CONTEO'] = dataframe[conteo]
    
    # Apply conditions dataframe
    for conditionKey in conditionsGeneral['conditionsData'].keys():
        print(f'Condition - {conditionKey}')
        
    
    # Calculate Basic Information
    # dataframe = calculateBasic.generateRates(dataframe=dataframe,
    #                                          columnsGroup=conditionsGeneral['columnsGroupBy'],
    #                                          columnCount=conteo,
    #                                          columnsPopulation=conditionsGeneral['columnsAddPopulations'],
    #                                          spatial=)
    
    
    
    return df_results
    