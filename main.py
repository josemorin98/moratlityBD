import time
from tools import handlingData


def main():
    print('Starting')
    # Start time
    startTime = time.time()
    
    # Specify the pattern of the files you want to read
    files_pattern = './utils/dataTest/*.csv'  # Adjust the pattern according to the file type
    
    # Specify the columns names of the files you want to read
    colums_select = ['ANIO_REGIS', 'ENT_OCURR', 'MUN_OCURR', 'CAUSA_DEF', 'SEXO' ,'EDAD']
    
    # Read the files in the directory
    dataResults = handlingData.read_csv_files(files_pattern=files_pattern,
                                              colums_select=colums_select)

    # Select only states data
    # NOTE: States with an ID greater than 32 are considered unknown and, therefore, are ignored.
    conditionState = {'ENT_OCURR':[32,'<=']}
    # Filter states by condition
    dataResults = handlingData.filter_data_conditions(dataframe=dataResults,
                                                      conditions=conditionState)
    # Return filtered states data
    print(f'Filtered states - count {len(dataResults.ENT_OCURR.unique())}')
    
    # Select only male and female
    # NOTE: Records with a 'Sex' ID equal to 9 are considered unknown and, therefore, are ignored.
    conditionSex = {'SEXO':[9,'!=']}
    # Filter sex by condition
    dataResults = handlingData.filter_data_conditions(dataframe=dataResults,
                                                      conditions=conditionSex)
    
    # Return filtered
    print(f'Filtered sex - count {len(dataResults.SEXO.unique())}')
    
    print(handlingData.add_age_by_column())
    
    # Start time
    endTime = time.time()
    print(f'Time to read: {(endTime-startTime)}')
    
if __name__ == "__main__":
    main()