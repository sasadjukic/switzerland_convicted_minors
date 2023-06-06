
import os, sys
import pandas as pd

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\swiss_convicted_minors_temp\main_data'
sys.path.append(file_path)

from data import swiss_2021 

# get all canton data fro 2021
cantons = swiss_2021[swiss_2021['canton_short'] != 'CH']

# get top 5 cantons with most minors convicted for 2021
top_5 = cantons.nlargest(5, columns='total_convicted')