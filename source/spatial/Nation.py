import pandas as pd
from  tools import handlingData, calculateRates
from progressbar import ProgressBar
from branchMortality import year

def welcome():
    print(f'This is the Nation')

def generateNation(dataframe,paramsNational):
    dfResults = pd.DataFrame()
    levels = 4
    with ProgressBar(max_value=len(levels)) as bar:
        runlevel=0
        
        # Get parameters for year and cause
        columnsGruops = paramsNational['YearCause']['ColumnGroups']
        columnCount = paramsNational['YearCause']['ColumnCount']
        
        # Generate mortality general
        dfResults = year.calculateGeneralMortality(dataframe=dataframe,
                                    columnsGruops=columnsGruops, 
                                    columnCount=columnCount)
        
        # Update progress bar
        runlevel += 1
        bar.update(runlevel)
        
    return dfResults