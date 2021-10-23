import numpy as np
import pandas as pd

data = pd.read_csv(r'')

class User:
    def __init__(self,id,username,password,name,year):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
        self.year = year

    def __init__(self,id):
