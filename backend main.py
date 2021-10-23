import numpy as np
import pandas as pd
import time
from datetime import datetime
import random as rng

current_ids = []
df = pd.read_csv(r'user data.csv')
data_col = pd.DataFrame(df, columns = ['ID']).to_numpy()
for x in range(data_col.size):
    current_ids.append(int(data_col[x][0]))
print(current_ids)
del df
del data_col

temp_str = ""

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

def new_user(username,password,name,year,classes):
    global temp_str
    temp_str = ""
    id = rng.randrange(99999999)
    while id in current_ids:
        id = rng.randrange(99999999)
    temp_str = str(id) + "," + username + "," + password + "," + name + "," + str(year) + "," + str(classes)
    with open('user data.csv','a') as fs:
        fs.write(temp_str[:-1])

def classes_to_str(classes):
    global temp_str
    temp_str = ""
    for x in range(len(classes)):
        temp_str += classes[x]
        temp_str += ":"
    return temp_str

jk = User(00000000)
print(jk)

evt1 = Event(1634956422,"Hack GT","CS 1331",jk,"Klaus")
print(evt1)

new_user("jkeller44@gatech.edu","dumbass45","Jack Keller",1,classes_to_str(["MATH 1554","ENGL 1101","CS 1100","CS 1331","POL 1101"]))
