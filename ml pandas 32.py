##loc function of Pandas used for accessing rows and columns by labels

import pandas as pd
df = pd.read_csv(r'C:\AKASH\numbers.csv')
print(df)

print('0th index pe jo hai uska value show ho rha hai',df.loc[0])
print('4th index pe jo hai uska value show ho rha hai',df.loc[4])

print('2nd and 4th ka value dega',df.loc[[2,4]])
print('4th index pe code ka value dega',df.loc[4,'n3'])
print('0th se 3rd index tak sab value milega',df.loc[0:3])

print('shows n4 column with values greater than 11 ',df.loc[df['n4']>11])

##iloc  is integer location-based indexing

print('0th index ka value print hoga',df.iloc[[0]])

##ye kaam loc se nahi hoga jo niche maine kiya hai
print('0th index ka sara column ka value print hoga kyuki [a=row,b=column]',df.iloc[:,0])
print(df.iloc[[0,1]])
