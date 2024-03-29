import pandas as pd

class Catalogs:
    def __init__(self):
        pass
        
    def get_edad(self) -> pd.DataFrame:
        """
        Retrieves age-related data from the EDADES.csv file.

        Returns:
        - pd.DataFrame: DataFrame containing age-related information.
        """
        return pd.read_csv("./utils/requeriments/EDADES.csv")\
            
    def get_population(self) -> pd.DataFrame:
        """
        Retrieves population data from the 'poblaciones_edad_state_new.csv' file.

        Returns:
        - pd.DataFrame: DataFrame containing population data.
        """
        return pd.read_csv("./utils/requeriments/poblaciones_edad_state_new.csv")
