import pandas as pd
import numpy as np

df = pd.read_csv('C:\AKASH\currency.csv')
print(df)

print("null value rahega to true likh ke aaega",df.isnull())

print("har ek column me kitna null value hai vo bataega",df.isnull().sum())

print("total kitna value hai null vo bataega ",df.isnull().sum().sum())

print("ye bataega kitna notnnull(achhe data) value hai ",df.notnull().sum().sum())

series1 = pd.Series([1,2,5,np.nan,6,np.NAN])
print("isnull() bataega ki kitna null values hai isme sum() ka value ",series1.isnull())






