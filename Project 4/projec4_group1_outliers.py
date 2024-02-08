import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

filename = 'AftrJuly15_RowsRemoved_1.csv'
df = pd.read_csv(filename)

data.plot(x=data.index.name, kind='box', figsize=(15,5))










#IQR
# Q1 = df.quantile(0.25)
# Q3 = df.quantile(0.75)
# IQR = Q3 - Q1
# print(IQR)
#
# print(df.shape)

# z = np.abs(stats.zscore(df))
# print(z)
#
# threshold = np.where(z > threshold)
# np.count_nonzero(z > 3)
# np.count_nonzero(z <= 3)
# data_dropped_outlier_z = data_dropped[(z <= 3).all(axis=1)]
# data_dropped_outlier_z.shape
