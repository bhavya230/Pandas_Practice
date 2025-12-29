# importing modules 
import pandas as pd 
import numpy as np
from io import StringIO

df= pd.read_csv('mercedesbenz.csv')
print(df) 
print(df.head())

#converting string to a in-memory file format using StringIO

data1=('col1,col2,col3\n'
      'x,y,1\n'
      'a,b,c')

file_formated_data=StringIO(data1)
df1=pd.read_csv(file_formated_data)
print(df1)

# when want to explore specific columns only 
print(pd.read_csv('mercedesbenz.csv',usecols=['X0','X1','X2','X3']))

# converting back to csv
print(df1.to_csv())

print(df1.to_csv(index=False)) # when dont want indexes to be converted

# assigning diff dataypes to diff columns
data2=('a,b,c,d\n'
       '1,2,3,4\n'
       '5,6,7,8\n'
       '9,10,11')

df2= pd.read_csv(StringIO(data2),dtype={'a':int,'b':float,'c':float})
print(df2.info())

#index col attribute -- tells which cols should be used as row index instead of default numbers-o,1,2.. 
data3= ('index,a,b,c\n'
        '4,apple,bat,5.7\n'
        '8,orange,cow,10')
df3=pd.read_csv(StringIO(data3))
print(df3)
df3=pd.read_csv(StringIO(data3),index_col='index')
print(df3)

# using usecols and index_cols iksth-- among columns seleceted in usecols index_cols is selected 
print(pd.read_csv(StringIO(data3),usecols=['a','b','c'] ,index_col='a')) 