import pandas as pd
from sklearn import datasets
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Load dataset
filename = 'CA_nurse_shortage.csv'
df = pd.read_csv(filename)
pd.set_option("display.max_rows", None, "display.max_columns", None)
data_dropped = df.dropna()

# Set feature and target
X = data_dropped[["Population", "Employed RNs", "Ratio"]]
Y = data_dropped[["Severity"]]

# only values in DataFrame returned
X = X.values
Y = Y.values.ravel()

# Initial prediction
clf = RandomForestClassifier()
clf.fit(X, Y)

# Divide into training and testing dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Train on new dataset
clf.fit(X_train, Y_train)

# Prediction on singular value
# print(clf.predict([[27424, 178, 649.1]]))
# print(clf.predict_proba([[27424, 178, 649.1]]))

# Prediction on test set
clf.predict(X_test)

# Performance testing
print(clf.score(X_test, Y_test))