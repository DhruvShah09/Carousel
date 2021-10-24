import numpy as np
import pandas as pd
import csv
import time
from tempfile import NamedTemporaryFile
import shutil
from datetime import datetime
import random as rng
from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash

#flask app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.secret_key = "bcasbhd31231923unazcnqbndubqsiubf"
#database stuff
current_ids = []
filename = r'user_data.csv'

df = pd.read_csv(filename)
data_col1 = pd.DataFrame(df, columns = ['ID']).to_numpy()
data_col2 = pd.DataFrame(df, columns = ['Username']).to_numpy()
for x in range(data_col1.size):
    current_ids.append([x,data_col1[x][0],data_col2[x][0]])
#print(current_ids)
del df
del data_col1
del data_col2

current_events = []
data = pd.read_csv(filename).to_numpy()

temp_str = ""
temp_arr = []
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
        self.events = str(data[row][6]).split(":")

    def __str__(self):
        return str(self.id) + ", " + self.username + ", " + self.password + ", " + self.name + ", " + str(self.year) + ", " + str(self.classes) + ", " + str(self.events)

class Event:
    def __init__(self,name,start_time,end_time,owner,location):
        self.id = int(rng.randrange(999999))
        for x in current_events:
            if x.id == id:
                self.id = int(rng.randrange(999999))
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.people = [owner.id]
        self.people_names = [owner.name]
        self.location = location
        for x in range(len(current_ids)):
            if owner in current_ids[x]:
                self.people_names = data[current_ids[x][0]][3]

class Study(Event):
    def __init__(self,name,start_time,end_time,owner,location,class_):
        super().__init__(name,start_time,end_time,owner,location)
        self.class_ = class_

    def __str__(self):
        return str(self.name) + ": " + str(datetime.utcfromtimestamp(self.start_time).strftime('%Y-%m-%d %H:%M:%S')) + " to " + str(datetime.utcfromtimestamp(self.end_time).strftime('%Y-%m-%d %H:%M:%S')) + ", Class: " + self.class_ + ", Partipants: " + str(self.people_names) + ", Location: " + self.location

class Sport(Event):
    def __init__(self,name,start_time,end_time,owner,location,sport):
        super().__init__(name,start_time,end_time,owner,location)
        self.sport = sport

    def __str__(self):
        return str(self.name) + ": " + str(datetime.utcfromtimestamp(self.start_time).strftime('%Y-%m-%d %H:%M:%S')) + " to " + str(datetime.utcfromtimestamp(self.end_time).strftime('%Y-%m-%d %H:%M:%S')) + ", Sport: " + self.sport + ", Partipants: " + str(self.people_names) + ", Location: " + self.location

def create_user_object(id):
    for x in range(len(current_ids)):
        if id in current_ids[x]:
            return User(id)

def get_row(username):
    for x in range(len(current_ids)):
        if username in current_ids[x]:
            return current_ids[x][0]

def get_id(username):
    for x in range(len(current_ids)):
        if username in current_ids[x]:
            return current_ids[x][1]

def get_username(id):
    for x in range(len(current_ids)):
        if id in current_ids[x]:
            return current_ids[x][2]

def get_user(name):
    for x in range(len(current_ids)):
        if name in current_ids[x]:
            return User(current_ids[x][0])

def get_event(id):
    for x in current_events:
        if x.id == id:
            return x

def get_event_index(id):
    for x in range(len(current_events)):
        if current_events[x].id == id:
            return x

def new_user(username,password,name,year,classes):
    global temp_str
    global data
    temp_str = ""
    id = int(rng.randrange(99999999))
    while id in current_ids:
        id = int(rng.randrange(99999999))
    temp_str = str(id) + "," + username + "," + password + "," + name + "," + str(year) + "," + str(classes) + ","
    with open(filename,'a') as fs:
        fs.write(temp_str+"\n")
    data = pd.read_csv(filename).to_numpy()
    current_ids.append([int(data.size/6-1),id,username])

def edit_user(id,arr):
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        writer = csv.writer(tempfile, delimiter=',', quotechar='"')
        for row in reader:
            if row[0] == str(id):
                row = arr
            writer.writerow(row)
    shutil.move(tempfile.name, filename)
    data = pd.read_csv(filename).to_numpy()

def add_event_to_user(id,arr,event):
    global temp_arr
    arr[6] = str(arr[6])
    temp_arr = arr
    if temp_arr[6] == None or temp_arr[6] == "nan":
        temp_arr[6] = str(event)
        edit_user(id,temp_arr)
    else:
        temp_arr[6] += ":" + str(event)
        edit_user(id,temp_arr)

def change_classes(id,new_classes):
    global temp_arr
    r = get_row(id)
    temp_arr = data[r]
    temp_arr[5] = new_classes
    edit_user(id,temp_arr)

def new_study(name,start_time,end_time,owner,location,class_):
    current_events.append(Study(name,start_time,end_time,owner,location,class_))
    add_event_to_user(owner.id,data[get_row(owner.id)],int(current_events[-1].id))

def new_sport(name,start_time,end_time,owner,location,sport):
    current_events.append(Sport(name,start_time,end_time,owner,location,sport))

def search_events(start_time,class_):
    global temp_arr
    temp_arr = []
    if start_time == None or class_ == None:
        return None
    for x in current_events:
        if start_time <= x.start_time and x.class_ == class_:
            temp_arr.append(x)
    return temp_arr

def get_event_ids(row):
    return data[row][6]

def push_event(events,num):
    if events == []:
        return None
    return events[num]

def join_event(user_id,event):
    for x in range(len(current_ids)):
        if user_id in current_ids[x]:
            add_event_to_user(user_id,data[current_ids[x][0]],event.id)
            event.people.append(user_id)
            event.people_names.append(data[current_ids[x][0]][3])

def get_user_classes(id):
    return create_user_object(id).classes

def login_query(username,password):
    global temp_index
    global data
    global row_
    temp_index = -1
    row_ = get_row(username)
    if data[row_][2] == password and data[row_][1] == username:
        return True
    else:
        return False

def date_to_unix(year,month,day,hour,minute):
    dt = datetime(year,month,day,hour,minute,0)
    return str(int(dt.replace().timestamp()))

def clear_expired_events():
    for x in current_events:
        if x.end_time >= time.time():
            current_events.remove(x)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        inp_name = request.form['name']
        inp_username = request.form['username']
        inp_password = request.form['password']
        inp_year = request.form['checkbox']
        inp_class = request.form.getlist('class')
        inp_class_string = ""
        for i in range(len(inp_class)):
            if i < len(inp_class)-1:
                inp_class_string = inp_class_string + str(inp_class[i]) + ":"
            else:
                inp_class_string = inp_class_string + str(inp_class[i])
        new_user(inp_username,inp_password,inp_name,inp_year,inp_class_string)
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        userName = request.form['username']
        pwd = request.form['password']
        if login_query(userName, pwd):
            session['login_state'] = True
            id_str = str(get_id(userName))
            print(id_str)
            session['user_id'] = id_str
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials'
            flash(error)
    return render_template('login.html')
@app.route('/usraccount', methods=['GET', 'POST'])
def usraccount():
    return render_template('account.html')
@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    return render_template('forgot.html')
#abstractions
@app.route('/homepage', methods=['GET', 'POST'])
def home():
    try:
        if session['login_state'] == True:
            usr = create_user_object(int(session['user_id']))
            tableval = []
            eventnames = []
            eventstarts = []
            eventends = []
            eventparticipants = []
            eventlocation = []
            eventclass = []
            for a in usr.events:
                temp_event = get_event(int(a))
                eventnames.append(temp_event.name)
                eventstarts.append(str(datetime.utcfromtimestamp(temp_event.start_time).strftime('%Y-%m-%d %H:%M:%S')))
                eventends.append(str(datetime.utcfromtimestamp(temp_event.start_time).strftime('%Y-%m-%d %H:%M:%S')))
                eventparticipants.append(temp_event.people_names)
                eventlocation.append(temp_event.location)
                eventclass.append(temp_event.class_)
                tableval.append(str(get_event(int(a))))
            iternum = len(eventnames)
            print(tableval)
            return render_template('homepage.html', eventnames=eventnames, eventstarts=eventstarts, eventends=eventends, eventparticipants=eventparticipants, eventlocation=eventlocation, eventclass=eventclass, iternum=iternum)
    except:
        return redirect(url_for('login'))
@app.route('/carousel', methods=['GET', 'POST'])
def carousel():
    if request.method == 'POST':
        start_time = request.form['start_time']
        end_time = request.form['end_time']

    return render_template('carousel.html')

def rideCarouselEventDisplay(time, class_, time_two, location):
    arr_to_display = search_events(time, class_)
    if arr_to_display == []:
        usr = create_user_object(int(session['user_id']))
        name = usr.name
        start_time = time
        end_time = time_two
        owner = usr.username
        loc = location
        arr_to_display.append(new_study(name, start_time, end_time, owner, loc, class_))
    return arr_to_display

#Testing code
#jk = User(00000000)
#print(jk)

<<<<<<< Updated upstream
#new_study("Linear Algebra Cram 1",1634970424,1634973424,get_user("jkeller44@gatech.edu"),"CULC","MATH 1554")
=======
new_study("Linear Algebra Cram 1",1634970424,1634973424,get_user("dshah374@gatech.edu"),"CULC","MATH 1554")
new_study("English Research Symposium",1634970424,1634973424,get_user("jkeller44@gatech.edu"),"Crosland Tower","ENGL 1102")
>>>>>>> Stashed changes
#print(current_events[-1])
#new_sport("Pickup Football",1634971424,1634974424,get_user("jkeller45@gatech.edu"),"Stamps Field","Football")
#print(current_events[-1])
#new_study("Linear Algebra Cram 3",1634961424,1634964424,get_user("jkeller45@gatech.edu"),"CULC","MATH 1554")
#new_sport("Linear Algebra Cram 4",1634981424,1634984424,get_user("jkeller45@gatech.edu"),"CULC","MATH 1554")
#print(get_user("jkeller44@gatech.edu"))
#print(current_events[0])
#print(current_events)
#print(current_events)
#print(get_user("jkeller44@gatech.edu"))
#print(current_events[0])
#print(get_event(current_events[0].id))

#print(User(55242536))
#print(search_events(1634970424,"MATH 1554"))
#print(current_events[-1])

#test loginquery
#print(loginQuery("jkeller44@gatech.edu", "dumbass45"))

#new_user("jkeller44@gatech.edu","dumbass45","Jack Keller",1,classes_to_str(["MATH 1554","ENGL 1101","CS 1100","CS 1331","POL 1101"])[:-1]+"\n")

#join_event(57579823,current_events[0])
#print(current_events[0])
def remove_event(compare, remove):
    with(open('user_data.csv', 'r', newline='')) as f:
        try:
            a = csv.reader(f, delimiter=',')
            axis = []
            for row in a:
                events = row[6].split(':')
                if str(compare) == row[0]:
                    events.remove(str(remove))
                    print(events)
                    event_str = ""
                    z = len(events)
                    for x in range(len(events)):
                        if x != z-1:
                            event_str = event_str + events[x] + ":"
                        else:
                            event_str = event_str + events[x]
                    row[6] = event_str
                axis.append(row)
            print(axis)
            with open('user_data.csv', 'w', newline='') as g: 
                b = csv.writer(g, delimiter=',')
                for row in axis:
                    b.writerow(row)
        except:
            pass
def flush_events():
    with(open('user_data.csv', 'r', newline='')) as f:
        try:
            a = csv.reader(f, delimiter=',')
            axis = []
            for row in a:
                events = row[6].split(':')
                print(events)
                event_str = ""
                row[6] = event_str
                axis.append(row)
            print(axis)
            with open('user_data.csv', 'w', newline='') as g: 
                b = csv.writer(g, delimiter=',')
                for row in axis:
                    b.writerow(row)
        except:
            pass

           
        
#edit_user(55242536,[55242536,"jkeller44@gatech.edu","dumbass46","Jack Keller",1,"MATH 1554:ENGL 1101:CS 1100:CS 1331:POL 1101",get_event_ids(get_row("jkeller44@gatech.edu"))])
#change_classes(55242536,"MATH 1554:ENGL 1101")
flush_events()
#print(current_ids)

#if __name__ == '__main__':
    #Threaded option to enable multiple instances for multiple user access support
    #app.run(threaded=True, port=5000)
