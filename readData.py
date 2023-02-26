import pandas as pd
from classGroup import Group
from personClass import Person
import calculatePts
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep

df = pd.read_excel('healthData.xlsx')
currentRow = 0

group_point_goal = 1000
group = Group([], group_point_goal, False)
for x in range(len(df)):
    personData = []
    ++currentRow
    for z in range(len(df.loc[x])):
        personData.append(df.loc[x][z])

    new_person = Person(personData[0], 0, personData[2],0, personData[1])
    calculatePts.calc_pts(new_person)
    group.add_friend(new_person)

calculatePts.calc_group_pts(group)


print(group.friends[0].name)
print(group.friends[0].points)
print(group.friends[1].name)
print(group.friends[1].points)
print(group.friends[2].name)
print(group.friends[2].points)
#delete previous data points in sheet to start over?


#start for loop from row you last ended at TODO
def update():
    for x in range(len(df)):
        personData = []
        ++currentRow
        for z in range(len(df.loc[x])): #start where previously stopped?
            personData.append(df.loc[x][z])

        for k in group.friends:
            if k == personData[0]:
                k.add_exercise_time(personData[3])
                calculatePts.calc_pts(k)

        calculatePts.calc_group_pts(group)

#link steps to kelly's function instead of my own

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
