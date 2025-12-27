# importing pandas and numpy
import pandas as pd
import numpy as np

# Series --- 

print(pd.Series([1,2,3])) # LIST

print(pd.Series(10,index=[1,2,3])) # SCALAR VALUE

print(pd.Series(np.array([4,5,6]), index=["one","two","three"])) #ndarray

dict={"name":"Bhavya","age":20}
print(pd.Series(dict)) # DICTIONARY

