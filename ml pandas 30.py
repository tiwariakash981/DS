##pandas interpolate function(only for numeric values)
import pandas as pd

df = pd.read_csv(r'C:\AKASH\numbers.csv',parse_dates=['Date'])
print(df)

ddf = df.infer_objects(copy=False)
print(ddf)

print("khudse assume karke automatic fill karega values ko\n",df.interpolate())
print("khudse assume karke automatic fill karega values ko\n",df.interpolate(method='linear'))

##datetime me change nahi ho rha hai thoda se dekh aur error solve kar  
df = pd.read_csv(r'C:\AKASH\numbers.csv',parse_dates=['Date'])
print("converting to date time ",df)

print("it is used for checking datatype",type(df.Date[0]))

##print('',df.interpolate(method='time'))

##df = pd.read_csv(r'C:\AKASH\numbers.csv',parse_dates=['Date'],index_col='n1')

print('isme index ko dkeh automatic fill karega index tujhe apne data load karne time batana padega ki konsa column hai index',df.interpolate(method='index'))
print('isme nearest value dekh ke automatic fill hoga',df.interpolate(method='nearest'))




