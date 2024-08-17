#Label encoding( done on ordinal,nominal) and OrderEncoding(done on ordinal variables) 
##categorical variable has two types:
##    1.Nominal variables
##    2.Ordinal variables

import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.max_rows',None)

df = pd.read_csv(r'C:\AKASH\datasets for ml\house prediction adv regression\train.csv')
print(df.columns)

df2 = df[['KitchenQual','BldgType']]  #df2 = df(['KitchenQual','BldgType']) isme round bracket mat use karna kyuki dataframe me se kuch value lena hota hai to kabhi bhi [] ye parenthesis use karte hai
le = LabelEncoder()
print(le.fit_transform(df2['BldgType']))
 
df2['BldgType_L_enc'] = le.fit_transform(df2['BldgType'])
print(df2)

print(df['BldgType'].value_counts())
print(df['KitchenQual'].value_counts())#here, ex=excellent,gd=good,ta=typical average,fa=fair

#aise humlog claass ko manual value bhi de sakte hai 
order_label = {'Ex':4,'Gd':3,'TA':2,'Fa':1}
print(r'printing order label for KitchenType',order_label)

df2['KitchenQual_org_enc']  =  df2['KitchenQual'].map(order_label)
print(df2)



