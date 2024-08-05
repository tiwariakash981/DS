## concat is used for adding two or more series,dataFrames this is part - II

import pandas as pd

df1 = pd.DataFrame({'id':[1,2,3,4],'name':['c','d','e','f'],'class':[7,8,10,11]})
print(df1)

df2 = pd.DataFrame({'id':[3,4],'name':['e','f'],'class':[5,6]})
print(df2)

df3 = pd.DataFrame({'Marks':[40,63,91,34]})
print(df3)

print('intersected values will be returned',pd.concat([df1,df2],axis=1,join='inner'))

print('assigning labels to df ',pd.concat([df1,df2],keys=['first_df','second_df']))
print('assigning labels to df ',pd.concat([df1,df2],keys=['first_df','second_df'],axis=1))

print('concatinating different data ',pd.concat([df1,df3]))












