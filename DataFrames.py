#  importing pandas and numpy
import pandas as pd 
import numpy as np

# Creating Data farmes 

# 1 using list
df1 = pd.DataFrame([1,2,3], index=["ROW 1 ","ROW 2", "ROW 3"],columns=["COLUMN 1"])
print(df1)
print("\n")

# 2 using series 
s= pd.Series(np.arange(5),index=["a","b","c","d","e"])
df2= pd.DataFrame(s,columns=["col1"])
print(df2)

# 3 using Dictionary 
dict={"Name":["Bhavya","Pushp","Nikita","Nalini"], "Age":[20,14,25,24]}
df3=pd.DataFrame(dict)
print(df3)

# 4 using  ndarrays
df4=pd.DataFrame(np.arange(20).reshape(5,4),index=["R1","R2","R3","R4","R5"],columns=["C1","C2","C3","C4"])
print(df4)