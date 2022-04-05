import json
import pandas as pd

#-- SERIES --#
#------------#  # It is a one-dimensional array holding data of any type.

a = [2, 4, 6]

myvar = pd.Series(a)

# print(myvar)

a = {
    'mal': 43,
    'tal': 568
}

myvar = pd.Series(a)

# print(myvar)



#-- DATAFRAMES --#
#----------------# #A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

var = {
    'name': ['720s Spider', 'Chiron', 'gtr', 'Lembo', 'ford gt heritage edition', 'henesi venom'],
    'value': [23, 32, 65, 75, 87, 24]
}

df = pd.DataFrame(var, index = ['x','e','v','h','f', 4])

# print(df)
# print(df.loc['x'])



#-- Read data files of diff types --#
#-----------------------------------#

# csv_file = pd.read_csv('data.csv')
# print(csv_file.to_string())

json_file = pd.read_json('data.json')
print(json_file.to_string())
