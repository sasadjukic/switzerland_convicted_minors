
# import necessary paths and libraries
import os, sys 
import matplotlib.pyplot as plt

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\swiss_convicted_minors_temp\country_data'
sys.path.append(file_path)

from national_data import (fourteen_and_under, 
                           fifteen,
                           sixteen,
                           seventeen
                        )


colors = ['#FF55BB', '#FFD3A3', '#FCFFB2', '#B6EAFA']

# create a pie chart
fig = plt.subplots()
plt.pie(
    [
     int(fourteen_and_under), int(fifteen),
     int(sixteen), int(seventeen)
    ],
    colors = colors,
    autopct = '%.2f %%'
)

# draw a circle to make it a doughnut pie chart
center_circle = plt.Circle((0, 0), 0.70, fc='#ffffff')
fig = plt.gcf()
fig.gca().add_artist(center_circle)

# show pie chart
plt.show()
