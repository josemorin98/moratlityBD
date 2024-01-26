import pandas as pd
from source.combinationsMortality import year_cause
from progressbar import ProgressBar


def calculateGeneralMortality(dataframe:pd.DataFrame, columnsGruops:list, columnCount:str, columnsPopulation:list) -> pd.DataFrame:
    print(f'Year')
    df_results = pd.DataFrame()
    
    # calculate year with cause
    df_results = year_cause.generateYearCause(dataframe=dataframe,
                                    columnsGruops=columnsGruops, 
                                    columnCount=columnCount,
                                    columnsPopulation=columnsPopulation)
    
    
    
    return df_results
    