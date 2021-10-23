import numpy as np
import pandas as pd
import csv
import time
from datetime import datetime
import random as rng
from flask import Flask, request, jsonify, render_template, redirect, url_for,session

#flask app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.secret_key = "bcasbhd31231923unazcnqbndubqsiubf"
#database stuff
current_ids = []
df = pd.read_csv(r'user data.csv')
data_col1 = pd.DataFrame(df, columns = ['ID']).to_numpy()
data_col2 = pd.DataFrame(df, columns = ['Username']).to_numpy()
for x in range(data_col1.size):
    current_ids.append([x,data_col1[x][0],data_col2[x][0]])
#print(current_ids)
del df
del data_col1
del data_col2

current_events = []
data = pd.read_csv(r'user data.csv').to_numpy()

temp_str = ""
temp_index = -1
row_ = -1

class User:
    def __init__(self,id):
        global data
        for x in range(len(current_ids)):
            if id in current_ids[x]:
                row = current_ids[x][0]
        self.id = data[row][0]
        self.username = str(data[row][1])
        self.password = str(data[row][2])
        self.name = str(data[row][3])
        self.year = data[row][4]
        self.classes = data[row][5].split(":")

    def __str__(self):
        return str(self.id) + ", " + self.username + ", " + self.password + ", " + self.name + ", " + str(self.year) + ", " + str(self.classes)

class Event:
    def __init__(self,name,start_time,end_time,class_,owner,location):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.class_ = class_
        self.people = [owner.id]
        self.people_names = [owner.name]
        self.location = location
        for x in range(len(current_ids)):
            if owner in current_ids[x]:
                self.people_names = data[current_ids[x][0]][3]

    def __str__(self):
        return str(self.name) + ": " + str(datetime.utcfromtimestamp(self.start_time).strftime('%Y-%m-%d %H:%M:%S')) + " to " + str(datetime.utcfromtimestamp(self.end_time).strftime('%Y-%m-%d %H:%M:%S')) + ", Class: " + self.class_ + ", Partipants: " + str(self.people_names) + ", Location: " + self.location

def new_user(username,password,name,year,classes):
    global temp_str
    global data
    temp_str = ""
    id = rng.randrange(99999999)
    while id in current_ids:
        id = rng.randrange(99999999)
    temp_str = str(id) + "," + username + "," + password + "," + name + "," + str(year) + "," + str(classes)
    with open(r'user data.csv','a') as fs:
        fs.write(temp_str)
    data = pd.read_csv(r'user data.csv').to_numpy()
    current_ids.append([int(data.size/6-1),id,username])

def edit_user(id,str):
    input = open(r'user data.csv','rb')
    output = open(r'user data edit.csv','wb')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[0] != str(id):
            writer.writerow(row)

def change_classes(id,new_classes):
    for x in range(len(current_ids)):
        if id in current_ids[x]:
            print("hi")

def classes_to_str(classes):
    global temp_str
    temp_str = ""
    for x in range(len(classes)):
        temp_str += classes[x]
        temp_str += ":"
    return temp_str

def new_event(name,start_time,end_time,class_,owner,location):
    current_events.append(Event(name,start_time,end_time,class_,owner,location))

def login_query(username,password):
    global temp_index
    global data
    global row_
    temp_index = -1
    for x in range(len(current_ids)):
        if username in current_ids[x]:
            row_ = current_ids[x][0]
    if data[row_][2] == password and data[row_][1] == username:
        return True
    else:
        return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        userName = request.form['username']
        pwd = request.form['password']
        if login_query(userName, pwd):
            session['login_state'] = True
            session['user_id'] = userName
            return "Succesfully Logged In"
        else:
            error = 'Invalid Credentials'
            return "Error Logging In"
    return render_template('login.html')

#Testing code
#jk = User(00000000)
#print(jk)

#new_event("Linear Algebra Cram",1634970424,1634973424,"MATH 1554",find_user("jkeller45@gatech.edu"),"CULC")
#print(current_events[-1])

#test loginquery
#print(loginQuery("jkeller44@gatech.edu", "dumbass45"))

#new_user("jkeller44@gatech.edu","dumbass45","Jack Keller",1,classes_to_str(["MATH 1554","ENGL 1101","CS 1100","CS 1331","POL 1101"])[:-1]+"\n")
#print(current_ids)

if __name__ == '__main__':
    #Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
