
import pandas as pd 

df = pd.read_csv('swiss.csv')

df.fillna(0, inplace=True)

df['male'] = df['male'].astype(int)
df['female'] = df['female'].astype(int)
df['14_and_younger'] = df['14_and_younger'].astype(int)
df['15_years_old'] = df['15_years_old'].astype(int)
df['16_years_old'] = df['16_years_old'].astype(int)
df['17_years_old'] = df['17_years_old'].astype(int)
df['swiss_nationals'] = df['swiss_nationals'].astype(int)
df['foreigners_b_c_ci_permit'] = df['foreigners_b_c_ci_permit'].astype(int)
df['other_foreigners'] = df['other_foreigners'].astype(int)
df['total_foreigners'] = df['total_foreigners'].astype(int)

df.to_csv('swiss_minors_convicted.csv', index=False)
