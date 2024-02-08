import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



filename = 'COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries_aftrJuly15.csv'
df = pd.read_csv(filename)
pd.set_option("display.max_rows", None, "display.max_columns", None)
data_dropped = df.dropna()


data_dropped.to_csv('AftrJuly15_RowsRemoved_1.csv')

print("Shape when null values have been removed: ")
print(data_dropped.shape)
print("Original shape: ")
print(df.shape)

