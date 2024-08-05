##merge in pandas
import pandas as pd

##df = pd.read_csv(r'C:/AKASH/currency1.csv')
##print(df)

df1 = pd.DataFrame({'id':[1,2,3,4],'name':['ak','bk','ck','dk']})
print(df1)

df2 = pd.DataFrame({'id':[1,2,3,5],'class':['aak','bbk','cck','ddk']})
print(df2)

df3 = pd.DataFrame({'id':[6,7,8,9],'class':['aak','bbk','cck','ddk']})
print(df3)

df4 = pd.DataFrame({'id':[1,2,3,4],'name':['ak','bk','ck','dk']})
print(df4)

##agar id ka length alag hota to sare values print nhi hote jo common values hote vo print ho jate 
print('merging df1,df2 using on for a common value ',pd.merge(df1,df2,on='id'))
print('merging df2,df1  but here df2 will be on left sideusing on for a common value ',pd.merge(df2,df1,on='id'))

##left ke jagah right bhi use kar sakta hai 
print('ye achhese tab samjhega jab df equal na ho in short left ka matlab left(df1) wale ke sare values print honge',pd.merge(df1,df2,on='id',how='left'))
print('isme right + left dono df ki values print hogi irrespective of the id ',pd.merge(df1,df2,on='id',how='outer'))
print('outer = dono df print karo,indicaotr=if same value exists then it will tell you',pd.merge(df1,df2,on='id',how='outer',indicator=True))

print('jab df me koi bhi index value same na ho tab ye use kar kyuki ye dono df ke value ko print karne me kaam aata hai\n',pd.merge(df1,df3,left_index=True,right_index=True))

##yaha first print statement me ye error hai ki column name khudse le rha hai to uske liye "suffixes" ka use kar 
print(pd.merge(df1,df4,on='id'))

print(pd.merge(df1,df4,on='id',suffixes=('_first','_second')))



