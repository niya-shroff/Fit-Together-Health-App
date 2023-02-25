import pandas as pd
from Group import Group
from Person import Person
import calculatePts

df = pd.read_excel('healthData.xlsx')

group_point_goal = 1000
group = Group([], group_point_goal, False)
for x in range(len(df)):
    personData = []
    for z in range(len(df.loc[x])):
        personData.append(df.loc[x][z])

    new_person = Person(personData[0], personData[1], personData[3],0, personData[2])
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

#every hour: TODO
for x in range(len(df)):
    personData = []
    for z in range(len(df.loc[x])): #start where previously stopped?
        personData.append(df.loc[x][z])

    for k in group.friends:
        if k == personData[0]:
            k.add_steps(personData[1])
            k.add_exercise_time(personData[3])
            calculatePts.calc_pts(k)


    new_person = Person(personData[0], personData[1], personData[3],0, personData[2])
    calculatePts.calc_pts(new_person)
    calculatePts.calc_group_pts(group)
