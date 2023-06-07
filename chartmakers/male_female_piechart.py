
# import necessary paths and libraries
import os, sys 
import matplotlib.pyplot as plt

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\swiss_convicted_minors_temp\country_data'
sys.path.append(file_path)

from national_data import male_convictions, female_convictions

# create necessary variables
colors = ['#B6EAFA', '#FF55BB']

# create a pie chart
fig = plt.subplots()
plt.pie(
    [int(male_convictions), int(female_convictions)],
    colors = colors,
    autopct = '%.2f %%',
    startangle = 45
)

# show pie chart
plt.show()