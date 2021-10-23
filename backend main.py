import numpy as np

class User:
    username = ""
    password = ""
    name = ""
    year = 0
    def __init__(self,username,password,name,year):
        self.username = username
        self.password = password
        self.name = name
        self.year = year
