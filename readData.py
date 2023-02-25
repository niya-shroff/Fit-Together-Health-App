import pandas as pd

df = pd.read_excel('healthData.xlsx')
fields = []

for col in df:
    fields.append(col)

print(fields)