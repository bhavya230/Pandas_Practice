import pandas as pd
from io import StringIO

data='{"employee_name": "james" , "email" : "james@gmail.com","job_profile":[{"title1": "Team lead", "title2": "Sr.Developer"}]}'

print(pd.read_json(StringIO(data)))

#orient attribute
# -- records
print(pd.read_json(StringIO(data),orient='records'))
#-- index
print(pd.read_json(StringIO(data),orient='index'))
#--split
#print(pd.read_json(StringIO(data),orient='split'))

# DataFrame to JSON OBJECT 
df=pd.DataFrame([['a','b'],['c','d']],index=['row1','row2'],columns=['col1','col2'])
print(df)
print(df.to_json())
# combining orient attribute
print(df.to_json(orient='index'))
print(df.to_json(orient='columns'))
print(df.to_json(orient='records'))
print(df.to_json(orient='split'))
print(df.to_json(orient='values'))

# JSON NORMALIZATION
data=[
  {
    "employee_name": "james",
    "email": "james@gmail.com",
    "job_profile": {
      "title1": "Team lead",
      "title2": "Sr.Developer"
    }
  }
]
print(pd.json_normalize(data))

data=[
    {         
        "id": 1,
        "name": "Cole Volk",
        "fitness": {"height": 130, "weight": 60},
    },
    {"name": "Mark Reg", "fitness": {"height": 130, "weight": 60}},
    {
        "id": 2,
        "name": "Faye Raker",
        "fitness": {"height": 130, "weight": 60},
    },
]
print(pd.json_normalize(data))

# maxlevel attribute -- to set depth of reading nested json objects
print(pd.json_normalize(data,max_level=0))
print(pd.json_normalize(data,max_level=1))