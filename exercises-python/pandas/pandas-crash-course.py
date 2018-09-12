import numpy as np
import pandas as pd

df = pd.read_csv('salaries.csv')
print(df)

#print(df['Salary'])
#print(df[['Name', 'Salary']])
#print(df['Salary'].min())


ser_of_bool = df['Age'] > 30
print(ser_of_bool)
print(df[ser_of_bool])

print(df[df['Age'] > 30])

print(df['Age'].unique())

print(df['Age'].nunique())

#print(df.columns)
#print(df.info())
#print(df.describe())
#print(df.index())

mat = np.arange(0,50).reshape(5,2)
print(mat)
df = pd.DataFrame(data=mat, columns=['A', 'B'])
print(df)