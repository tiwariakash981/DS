## using append function

import pandas as pd

df1 =  pd.DataFrame({'a':[1,2,3],'b':[10,20,30]})
print(df1)

df2 =  pd.DataFrame({'a':[4,5,6],'b':[40,50,60]})
print(df2)

df3 =  pd.DataFrame({'c':[4,5,6],'d':[40,50,60]})
print(df3)

print(df1._append(df2))

print('ignoring indexes',df2._append(df1,ignore_index=True))

print('ignoring indexes',df2._append(df3,ignore_index=True))





















