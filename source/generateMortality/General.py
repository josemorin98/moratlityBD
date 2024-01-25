import pandas as pd
from branchMortality import year
from progressbar import ProgressBar


def calculateGeneralMortality(dataframe:pd.DataFrame, columnsGruops:list, columnCount:str) -> pd.DataFrame:
    print(f'Year')
    df_results = pd.DataFrame()
    
    # calculate year with cause
    df_results = year.generateYear(dataframe=dataframe,
                                    columnsGruops=columnsGruops, 
                                    columnCount=columnCount)
    
    
    
    return df_results
    