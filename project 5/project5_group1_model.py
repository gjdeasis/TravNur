#imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# Load dataset
filename = 'AftrJuly15_RowsRemoved_1.csv'
df = pd.read_csv(filename)
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Set feature and target
X = df[["total_adult_patients_hospitalized_confirmed_covid", "total_pediatric_patients_hospitalized_confirmed_covid"]]
Y = df[["critical_staffing_shortage_today_yes"]]



#data.plot(kind='scatter', x='critical_staffing_shortage_today_yes', y='critical_staffing_shortage_anticipated_within_week_yes')
#data.boxplot(column=['critical_staffing_shortage_today_yes', 'critical_staffing_shortage_anticipated_within_week_yes'])
#plt.show()
#print(data.corr()
#
# shortToday=pd.DataFrame(data['critical_staffing_shortage_today_yes'])
# shortNxWk=pd.DataFrame(data['critical_staffing_shortage_anticipated_within_week_yes'])
#
# lm= linear_model.LinearRegression()
# model = lm.fit(shortToday,shortNxWk)
# model.coef_
# model.intercept_
# model.score(shortToday, shortNxWk)
# tod_short = 27
# short_predict = model.predict([[tod_short]])
# print(short_predict)
#
# data.plot(kind='scatter', x='critical_staffing_shortage_today_yes', y='critical_staffing_shortage_anticipated_within_week_yes')
# plt.plot(shortToday,model.predict(shortToday), color='red',linewidth=2)
# plt.scatter(tod_short, short_predict, color='black')
# plt.show()