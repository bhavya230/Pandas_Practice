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