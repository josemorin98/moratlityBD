import pandas as pd
from  tools import handlingData, calculateRates
from progressbar import ProgressBar
from source.generateMortality import General

def welcome():
    print(f'This is the Nation')

def generateNation(dataframe:pd.DataFrame,paramsNational:dict):
    """
    Generates different combinations of data to calculate rates of Nation.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing the data.
    - params_national (dict): A dictionary containing parameters for generating national data combinations.

    Returns:
    - DataFrame: A DataFrame with different combinations of data for rate calculation.
    """
    dfResults = pd.DataFrame()
    levels = 4
    with ProgressBar(max_value=levels) as bar:
        runlevel=0
        
    # GENERAL
    #========================================================================
        
        #--------------------------------------------------------------------
        # Get parameters for year and cause
        columnsGruops = paramsNational['YearCause']['columnsGroups']
        columnCount = paramsNational['YearCause']['columnCount']
        columnsPopulations = paramsNational['YearCause']['columnsGroupPopulation']
        
        # Generate mortality general
        dfResults = General.calculateGeneralMortality(dataframe=dataframe,
                                    columnsGruops=columnsGruops, 
                                    columnCount=columnCount,
                                    columnsPopulation=columnsPopulations)
        
        # Fill columns with all (Total)
        dfResults['ENT_CVE'] = 'Total'
        dfResults['MUN_CVE'] = 'Total'
        dfResults['RANGO_EDAD'] = 'Total'
        
        # Sort columns
        dfResults = dfResults.reindex(columns=['CAUSA_DEF','ANIO_REGIS','ENT_CVE','MUN_CVE','SEXO','RANGO_EDAD','CONTEO','POBLACION'])

        # Put rates
        dfResults = calculateRates.calculate_crude_rates(dataframe=dfResults, population='POBLACION', count='CONTEO')

        #--------------------------------------------------------------------
        #Get parameters for year, cause, sex
        
        
        
        
    #  CHAPTER
    #========================================================================
        
        
        
    #  CIE GENERAL
    #========================================================================
        
        
        
    #  CIE SPECIFIC
    #========================================================================
        
        
        
        
        
        # Update progress bar
        runlevel += 1
        bar.update(runlevel)
        
    return dfResults