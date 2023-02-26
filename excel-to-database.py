import csv
import pymongo
import pandas as pd

read_file = pd.read_excel("T1.xls") #add new excel file here
read_file.to_csv("Test.csv",
                  index=None,
                  header=True)
df = pd.read_excel("T1.xlsx") #need to change this

connection = pymongo.MongoClient('127.0.0.1:27017')
db = connection.test
collection = db.table1
table = open('Test.csv', 'r')
reader = csv.DictReader(table)
#collection.drop()
header = df.head()

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]
    collection.insert_one(row)
