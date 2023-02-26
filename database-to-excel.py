import subprocess
import pandas as pd
from Group import Group
from Person import Person
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep

def getPersonCollection(path: str): 
    subprocess.run("mongoexport --db admin --collection import1 --out personCollection.csv cat personCollection.csv", shell = True)

def getGroupCollection(path: str): 
    subprocess.run("mongoexport --db admin --collection import2 --out groupCollection.csv cat groupCollection.csv", shell = True)

def getMemberCollection(path: str): 
    subprocess.run("mongoexport --db admin --collection import3 --out memberCollection.csv cat memberCollection.csv", shell = True)
