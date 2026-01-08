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
print(pd.read_json(StringIO(data),orient='split'))
