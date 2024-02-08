# Imports
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn.model_selection import train_test_split

# Load Dataset
filename = 'AftrJuly15_RowsRemoved_1.csv'
df = pd.read_csv(filename)
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Set feature and target, create X and Y
X = df[["critical_staffing_shortage_anticipated_within_week_yes", "total_pediatric_patients_hospitalized_confirmed_and_suspected_covid", "total_adult_patients_hospitalized_confirmed_and_suspected_covid", "total_adult_patients_hospitalized_confirmed_covid", "total_pediatric_patients_hospitalized_confirmed_covid"]]
Y = df[["critical_staffing_shortage_today_yes"]]


# Split dataset into testing and training sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

# Create and train linear regression model
model = linear_model.LinearRegression()
model.fit(X_train, Y_train)

# Test model
Y_pred = model.predict(X_test)
print(Y_pred)

# Accuracy Testing
print(r2_score(Y_test, Y_pred))