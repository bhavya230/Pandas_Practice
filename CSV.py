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
print(pd.read_csv(file_formated_data))