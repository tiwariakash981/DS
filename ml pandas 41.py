## Date agar object me hai to Datetime me karne ke liye ye code hai
import pandas as pd

##df = pd.read_csv(r'C:\AKASH\currency1.csv')
##print(df)
##
##print(df.dtypes)
##print(type(df.Date1[0]))

df1 = pd.read_csv(r'C:\AKASH\currency1.csv',parse_dates=['Date1'])
print(df1)
print('updated',df1.dtypes)
print('123 \n',type(df1.Date1[11]))
