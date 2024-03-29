import pandas as pd
from sklearn import datasets
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Load dataset
filename = 'AftrJuly15_RowsRemoved_1.csv'
df = pd.read_csv(filename)
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Set feature and target
# X = df[["critical_staffing_shortage_today_yes", "total_adult_patients_hospitalized_confirmed_covid", "total_pediatric_patients_hospitalized_confirmed_covid"]]
# Y = df[["critical_staffing_shortage_anticipated_within_week_yes"]]

X = df[["critical_staffing_shortage_anticipated_within_week_yes", "total_adult_patients_hospitalized_confirmed_covid", "total_pediatric_patients_hospitalized_confirmed_covid"]]
Y = df[["critical_staffing_shortage_today_yes"]]

# only values in DataFrame returned
X = X.values
Y = Y.values.ravel()

# Initial prediction
clf = RandomForestClassifier()
clf.fit(X, Y)
# print(clf.feature_importances_)
# X[0]
# print(clf.predict([[2, 43, 0]]))
# print(clf.predict(X[[0]]))
# print(clf.predict_proba(X[[0]]))

# Divide into training and testing dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

# Train on new dataset
clf.fit(X_train, Y_train)

# Prediction on singular value
print(clf.predict([[2, 43, 0]]))
print(clf.predict_proba([[2, 43, 0]]))

# Prediction on test set
print(clf.predict(X_test))
print(Y_test)

# Performance
print(clf.score(X_test, Y_test))