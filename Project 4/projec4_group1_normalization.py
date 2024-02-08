import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

filename = 'AftrJuly15_RowsRemoved_1.csv'
df = pd.read_csv(filename)

df['critical_staffing_shortage_anticipated_within_week_yes'].head()
df['critical_staffing_shortage_anticipated_within_week_yes'].hist()
mean = df['critical_staffing_shortage_anticipated_within_week_yes'].mean()
std = df['critical_staffing_shortage_anticipated_within_week_yes'].std()
df['critical_staffing_shortage_anticipated_within_week_yes'].mean(), df['critical_staffing_shortage_anticipated_within_week_yes'].std()



z_score = (df['critical_staffing_shortage_anticipated_within_week_yes'] - mean)/std
z_score.head()
z_score.mean(), z_score.std()
print("%.3f" % z_score.mean())
print("%.3f" % z_score.std())

z_score.hist()

plt.show()