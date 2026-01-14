# HOW TO READ HTML FILES WITH THE HELP OF PANDAS 
import pandas as pd

html=pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code") # reads tables from html pages
print(type(html)) # list 
print(html) # prints list of all tables 

print(html[0]) # get 1st table 
type(html[0]) # each table would be a DATAFRAME

# match parameter -- to get specific table
html=pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code",match="Government debt")
print(html[0])

# converting back to html
html[0].to_html('demo.html')