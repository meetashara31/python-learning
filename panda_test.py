import json
from numpy import true_divide
import pandas as pd

#-- SERIES --#
#------------#  # It is a one-dimensional array holding data of any type.
def series_exm():
    a = [2, 4, 6]

    myvar = pd.Series(a)

    # print(myvar)

    a = {
        'mal': 43,
        'tal': 568
    }

    myvar = pd.Series(a)

    print(myvar)

#-- DATAFRAMES --#
#----------------# #A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

def dframe_exm():
    var = {
        'name': ['720s Spider', 'Chiron', 'gtr', 'Lembo', 'ford gt heritage edition', 'henesi venom'],
        'value': [23, 32, 65, 75, 87, 24]
    }

    df = pd.DataFrame(var, index = ['x','e','v','h','f', 4])

    print(df)
    print(df.loc['x'])



#-- Read data files of diff types --#
#-----------------------------------#

def read_file():
    csv_file = pd.read_csv('data/data.csv')
    print(csv_file.to_string())

    json_file = pd.read_json('data/data.json')
    print(json_file.to_string())


def data_cleaning():
    df = pd.read_csv('data/dirtydata.csv')

    #remove the raw containing NULL value
    # new_df = df.dropna()
    # new_df.to_csv('data/cleaneddata.csv')
    # print(new_df)

    #inplace dont return anything
    # df.fillna(130, inplace=True)
    # print(df)

    # m = df['Calories'].mean()
    # df['Calories'].fillna(m, inplace=True)

    #Fromate
    # df['Date'] = pd.to_datetime(df['Date'])
    # print(df)
    


##----- MAIN -----##
##----------------##
# series_exm()
# dframe_exm()
# read_file()
data_cleaning()
