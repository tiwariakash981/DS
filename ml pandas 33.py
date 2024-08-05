##pandas groupby function used to split data 

import pandas as pd
df = pd.read_csv(r'C:\AKASH\currency1.csv')
print('original data \n',df)


gr1 = df.groupby(by='Area')
print(gr1)

print('making groups for Code section',gr1.groups)

gr2 = df.groupby(['Area','Date'])
print('Area aur Date wale column ka grp ban gaya hai ',gr2.groups)


for Area,i in gr1:
    print('iterating in Code section\n',Area)
    print('iterating in actual values\n',i)

print('converting to list \n',list(gr1))
print('now converting to dictionary\n',dict(list(gr1)))

print('Date column me jiska value yes rahega uska ek grp banega',df.groupby('Date').get_group('yes'))

print('agar values rahega to sum hoga',gr1.sum())
##print('for calculating mean',gr1.mean())
print('count,min,max,in percentagee ye sab values ek hi baar me milega',gr1.describe())


## ye niche alag alag values ko dikha sakta hai for numeric data
print('',gr1.agg['min','sum','max'])
















