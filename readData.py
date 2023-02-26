import subprocess
import pandas as pd
from Group import Group
from Person import Person
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep

#this group's points must be updated
    person1 = Person("Niya", 0, 0, 0, 0, 100)
    person2 = Person("Kelly", 0, 0, 0, 0, 100)
    group = Group([person1, person2], 1000, False)

def update():
    for x in group:
        steps = parse_step_CSV('data/healthData.xlsx')
        x.addSteps(steps)
        timeExercised = parse_exercise_time('data/healthData.xlsx')
        x.add_exercise_time(timeExercised)
        x.calc_group_pts(x)

sched = BackgroundScheduler()
sched.add_job(update, 'interval', seconds = 3600)
sched.start()

while True:
    sleep(1)

#called every hour
#takes in a path to a csv file (with the step data) and returns the number of steps taken in the last hour
def parse_step_CSV(path: str):
    subprocess.run("heartbridge", shell = True) #run command in terminal to send step CSV to this folder

    df1 = pd.read_csv(path)
    rows = len(df1)
    df2 = pd.read_csv(path, index_col = False, skiprows = rows -  1) #get last row of csv (data from last hour)
    last_row = df2.to_string(index = False)
    arr = last_row.split()
    print(arr)
    return int(arr[5]) #steps from last hour

#example: parse_step_CSV("/Users/kdeng/Downloads/Hackher/steps-Feb24-2023.csv")

def parse_exercise_time(path: str):
    df = pd.read_csv(path, index_col = False, skiprows = 1)
    s = df.to_string(index = False)
    arr = s.split()
    exercise_time = 0
    for bpm in arr:
        if int(bpm) > 130:
            exercise_time += 1
    return exercise_time #exercise_time from last hour

#parse_exercise_time("/Users/kdeng/Downloads/Hackher/testBPM.csv")
