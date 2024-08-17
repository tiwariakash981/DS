#X=independent variable y = dependent variable X matrix me  aur y vector me rakhte hai
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split

#What is dpendent and independent between X,y and why they are use

df = sns.load_dataset('titanic')
df2 = df[['survived','pclass','age','parch']]
df3 = df2.fillna(df2.mean())
print(df3)

X = df3.drop('survived',axis=1)
y = df3['survived']
print(X.shape)
print(y.shape)#iska aur X_train ka shape check kar

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=51)#agar random state ka use nhi karunga to data hamesha randomly X_train ko milta rahega constant nhi rahega aur agar random state use karega to ek hi data milega X_train ko aur  test wale ko bhi
print('Shape of X_train',X_train.shape)#iska aur X_train ka shape check kar
print('Shape of X_test',X_test.shape)
print('Shape of y_train',y_train.shape)
print('Shape of y_test',y_test.shape)

print(X_train)



