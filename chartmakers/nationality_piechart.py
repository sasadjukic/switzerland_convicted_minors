
# import necessary paths and libraries
import os, sys 
import matplotlib.pyplot as plt

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\swiss_convicted_minors_temp\country_data'
sys.path.append(file_path)

from national_data import swiss_nationals, foreigners 

# create necessary variables
colors = ['#B6EAFA', '#FFD3A3']

# create a pie chart
fig = plt.subplots()
plt.pie(
    [int(swiss_nationals), int(foreigners)],
    colors = colors,
    autopct = '%.2f %%',
    startangle = 70
)

# show pie chart
plt.show()