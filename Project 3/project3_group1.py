import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



filename = 'COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries_aftrJuly15.csv'
df = pd.read_csv(filename)
pd.set_option("display.max_rows", None, "display.max_columns", None)

print("Statistical Description")
print(df.dtypes)
print(df.shape)
print(df.info())
print(df.describe()) #summary statistics (includes min, max, mean, count, std, 25%, 50%, 75%,)
print(df.corr())

print("Skewness")
print(df.skew(axis = 0, skipna = True))

print('Class Distribution')
#Univariate Plots
df.boxplot()
df.hist()

# sns.distplot(df['critical_staffing_shortage_today_yes'])
# sns.distplot(df['critical_staffing_shortage_anticipated_within_week_yes'])
# sns.distplot(df['total_adult_patients_hospitalized_confirmed_and_suspected_covid'])
# sns.distplot(df['total_adult_patients_hospitalized_confirmed_covid'])
# sns.distplot(df['total_pediatric_patients_hospitalized_confirmed_and_suspected_covid'])
# sns.distplot(df['total_pediatric_patients_hospitalized_confirmed_covid'])


#Multivariate Plots
#Note: Because we ran into errors, we created a dataset containing only the 6 variables of interest and created scatterplots for that file. See submission for other file.

# df.plot(kind = 'scatter', x = 'criticial_staffing_shortage_shortage_today_yes', y = 'critical_staffing_shortage_anticipated_within_week_yes')
# df.plot(kind = 'scatter', x = 'total_pediatric_patients_hospitalized_confirmed_covid', y = 'critical_staffing_shortage_anticipated_within_week_yes')
# df.plot(kind = 'scatter', x = 'total_pediatric_patients_hospitalized_confirmed_covid', y = 'total_adult_patients_hospitalized_confirmed_and_suspected_covid')

plt.show()

