# importing modules 
import pandas as pd 
import numpy as np
from io import StringIO

df= pd.read_csv('mercedesbenz.csv')
print(df) 
print(df.head())

#converting string to a in-memory file format using StringIO

data=('col1,col2,col3\n'
      'x,y,1\n'
      'a,b,c')

file_formated_data=StringIO(data)
df1=pd.read_csv(file_formated_data)
print(df1)

# when want to explore specific columns only 
print(pd.read_csv('mercedesbenz.csv',usecols=['X0','X1','X2','X3']))

# converting back to csv
print(df1.to_csv())

print(df1.to_csv(index=False)) # when dont want indexes to be converted