import pandas as pd

class Catalogs:
    def __init__(self):
        pass
        
    def get_edad(self):
        return pd.read_csv("./utils/requeriments/EDADES.csv")
    
        