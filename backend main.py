import numpy as np
import pandas as pd
import time
from datetime import datetime

class User:
    def __init__(self,id):
        df = pd.read_csv(r'user data.csv')
        data_col = pd.DataFrame(df, columns = ['ID']).to_numpy()
        data = df.to_numpy()
        for x in range(data_col.size):
            if data_col[x][0] == 0:
                row = x
        self.id = data[row][0]
        self.username = str(data[row][1])
        self.password = str(data[row][2])
        self.name = str(data[row][3])
        self.year = data[row][4]
        self.classes = data[row][5].split(":")

    def __str__(self):
        return str(self.id) + ", " + self.username + ", " + self.password + ", " + self.name + ", " + str(self.year) + ", " + str(self.classes)

class Event:
    def __init__(self,time,name,class_,owner,location):
        self.time = time
        self.name = name
        self.class_ = class_
        self.people = [owner]
        self.people_names = [owner.name]
        self.location = location

    def __str__(self):
        return str(self.name) + ": " + str(datetime.utcfromtimestamp(self.time).strftime('%Y-%m-%d %H:%M:%S')) + ", Class: " + self.class_ + ", Partipants: " + str(self.people_names) + ", Location: " + self.location

jk = User(0)
print(jk)

evt1 = Event(1634956422,"Hack GT","CS 1331",jk,"Klaus")
print(evt1)
