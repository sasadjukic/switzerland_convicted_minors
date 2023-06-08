
# import necessary paths and libraries
import os, sys 
import matplotlib.pyplot as plt

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\swiss_convicted_minors_temp\country_data'
sys.path.append(file_path)

from canton_data import top_5 

# create necessary variables
color = '#B6EAFA'
cantons = top_5['canton'].tolist()
values = top_5['total_convicted'].tolist()

# reverse array values to show highest first
cantons.reverse()
values.reverse()

# create a bar chart
fig, ax = plt.subplots()

plt.barh(
    cantons,
    values,
    color=color
)

# modify the looks 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# show bar values
for index, value in enumerate(values):
        plt.text(
            index, 
            value,
            str(value),
            position = (value+100, index)
        )


# show bar chart
plt.show()


