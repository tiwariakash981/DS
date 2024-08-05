##Melt function used for reshaping data

import pandas as pd

df1 = pd.read_csv(r'C:\AKASH\currency1.csv')
print(df1)

print('df i provided in long format ',pd.melt(df1))

print('area ke hisaab se value milega',pd.melt(df1,id_vars='Area'))

##unnpivot=print('area ke hisaab se value milega',pd.melt(df1,id_vars='Area'))
##unpivot = columns ko row me karna zada columns ko kam columns banana

print('area ke hisaab se value milega + symbol bhi',pd.melt(df1,id_vars='Area',value_vars=['Symbol']))

print('changes  the column name',pd.melt(df1,id_vars='Area',var_name='Category'))

