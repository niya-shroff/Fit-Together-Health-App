import subprocess

import pandas as pd
from Person import Person
niya = Person("Niya", 8000, "60 Minutes", 20, 120, "60 Mins", "10%")

def calc_steps_from_csv():
    subprocess.run("heartbridge", shell=True)
    dfNiyaSteps = pd.read_csv('steps-Feb24-2023-Feb25-2023.csv', index_col=0)
    stepsArr = dfNiyaSteps.to_string(index=False).split()
    stepsArr = stepsArr[1:]
    count = 0

    for str in stepsArr:
        num = int(str)
        count += num
    print(count)

calc_steps_from_csv()