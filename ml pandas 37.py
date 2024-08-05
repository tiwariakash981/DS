## pandas join function
##NOTE DATASET ME SAME NAAM SE COLUMN RAHEGA TO ERROR AAEGA
import pandas as pd

df1 = pd.DataFrame({'a':[1,2,3],'b':[10,20,30]},index=['a','b','c'])
print(df1)

df2 = pd.DataFrame({'c':[4,5,6],'d':[40,50,60]},index=['a','b','c'])
print(df2)

df3 = pd.DataFrame({'c':[4,5],'d':[40,50]},index=['a','b'])
print(df3)

##print(display(df1,df2))

print('df1 aur df2 me index same rehna chahiye nahi to join nhi hoga ',df1.join(df2))

print('aisa karega to NaN dikhaega usko solve karne ke liye niche likha hu ',df1.join(df3))
print('dono ka values dikhaega = union ',df1.join(df3),how='outer')
print('right=df3 ke hisaab se print hoga data ',df1.join(df3),how='right')

print('lsuffix used to assign a column name ',df1.join(df3),lsuffix='_1',how=''inner)

















