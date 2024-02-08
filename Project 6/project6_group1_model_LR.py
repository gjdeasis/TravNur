# Imports
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn.model_selection import train_test_split

# Load Dataset
filename = 'nationwide_nurse_shortage.csv'
df = pd.read_csv(filename)
pd.set_option("display.max_rows", None, "display.max_columns", None)

print(df.shape)
# Drop null values
data_dropped = df.dropna()

# Set feature and target, create X and Y

# Model 1
# X = data_dropped[["total_adult_patients_hospitalized_confirmed_covid", "total_pediatric_patients_hospitalized_confirmed_covid"]]
# Y = data_dropped[["critical_staffing_shortage_today_yes_wkLtr"]]

# Model 2
X = data_dropped[["critical_staffing_shortage_anticipated_within_week_yes", "total_adult_patients_hospitalized_confirmed_covid", "total_pediatric_patients_hospitalized_confirmed_covid"]]
Y = data_dropped[["critical_staffing_shortage_today_yes_wkLtr"]]

# Model 3
# X = data_dropped[["critical_staffing_shortage_anticipated_within_week_yes", "total_pediatric_patients_hospitalized_confirmed_and_suspected_covid", "total_adult_patients_hospitalized_confirmed_and_suspected_covid", "total_adult_patients_hospitalized_confirmed_covid", "total_pediatric_patients_hospitalized_confirmed_covid"]]
# Y = data_dropped[["critical_staffing_shortage_today_yes_wkLtr"]]


# Split dataset into testing and training sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Create and train linear regression model
model = linear_model.LinearRegression()
model.fit(X_train, Y_train)

# Test model
Y_pred = model.predict(X_test)
# Y_pred = model.predict(X_train)

# Accuracy Testing
print(r2_score(Y_test, Y_pred))
# print(r2_score(Y_train, Y_pred))