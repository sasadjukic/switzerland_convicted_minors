
import pandas as pd 
from pathlib import Path 

directory = Path(__file__).parents[1]
file = directory / 'swiss_minors_convicted.csv'

# import csv file
df = pd.read_csv(file)

# drop columns that have no values
swiss = df.dropna()

# convert selected columns to integer values
for column in swiss.columns[6:11]:
    swiss[column] = swiss[column].astype(int)

for column in swiss.columns[12:]:
    swiss[column] = swiss[column].astype(int)

# focus on 2021
swiss_2021 = swiss[swiss['year'] == 2021]



