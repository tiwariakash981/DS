##concat (used for combining series,dataFrame )
import pandas as pd

sr1 = pd.Series([1,2,3])
print(sr1)

sr2 = pd.Series([4,5,6,7])
print(sr2)

print(pd.concat([sr1,sr2]))

df1 = pd.DataFrame({'id':[1,2,3,4],'name':['a','b','c','d'],'class':[5,6,7,8]})
df2 = pd.DataFrame({'id':[5,6,7,8],'name':['e','f','g','h'],'class':[9,10,11,12]})

print('concatinating',pd.concat([df1,df2]))
print('axis=1=column wise concat',pd.concat([df1,df2],axis=1))

print('axis=0=row wise concat but isme index value me dekhna pblm aaega isliye niche ignore_index use kiya hai',pd.concat([df1,df2],axis=0))

print('ignoring indexes value',pd.concat([df1,df2],axis=0,ignore_index=True))
