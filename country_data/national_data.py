
# import necessary paths and libraries
import os, sys

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\swiss_convicted_minors_temp\main_data'
sys.path.append(file_path)

from data import swiss_2021

# get national data for 2021
national = swiss_2021[swiss_2021['canton_short'] == 'CH']

# male & female convictions
male_convictions = national['male']
female_convictions = national['female']

# swiss nationals & foreigners convictions
swiss_nationals = national['swiss_nationals']
foreigners = national['total_foreigners']

# convictions sorted by age
fourteen_and_under = national['14_and_younger']
fifteen = national['15_years_old']
sixteen = national['16_years_old']
seventeen = national['17_years_old']