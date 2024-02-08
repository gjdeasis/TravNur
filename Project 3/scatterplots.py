import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('UpdatedCovidFile.csv')

df = df.fillna('0')

df_1 = df['total_adult_patients_hospitalized_confirmed_and_suspected_covid'].str.replace(",","")
df_2 = df['total_adult_patients_hospitalized_confirmed_covid'].str.replace(",","")
df_3 = df['total_pediatric_patients_hospitalized_confirmed_and_suspected_covid'].str.replace(",","")

pd.to_numeric(df_1)
pd.to_numeric(df_2)
pd.to_numeric(df_3)
df_1 = df_1.astype(int)
df_2 = df_2.astype(int)
df_3 = df_3.astype(int)

df['total_adult_patients_hospitalized_confirmed_and_suspected_covid'] = df_1
df['total_adult_patients_hospitalized_confirmed_covid'] = df_2
df['total_pediatric_patients_hospitalized_confirmed_and_suspected_covid'] = df_3


#print("It is converted to: ",df_2.dtype)
df.plot(kind = 'scatter', x = 'total_adult_patients_hospitalized_confirmed_covid', y = 'critical_staffing_shortage_anticipated_within_week_yes')
df.plot(kind = 'scatter', x = 'total_adult_patients_hospitalized_confirmed_covid', y = 'total_adult_patients_hospitalized_confirmed_and_suspected_covid')
plt.show()
#print(df.dtypes.to_string())

