# importing pandas and numpy
import pandas as pd
import numpy as np

# Series --- 

s1=pd.Series([1,2,3]) # LIST
print(s1)

s2=pd.Series(10,index=[1,2,3]) # SCALAR VALUE
print(s2)

s3=pd.Series(np.array([4,5,6]), index=["one","two","three"]) #ndarray
print(s3)

dict={"name":"Bhavya","age":20}
s4=pd.Series(dict) # DICTIONARY
print(s4)

# Head function 

print ( s1.head(2))
print(s2.head(1))

# Tail function 
print(s3.tail(2))
print(s4.tail(1))