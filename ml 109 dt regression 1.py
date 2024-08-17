print('\n Decision tree me zadatar CART algorithm use karte hai ye tutorial Regression ke liye use kar rhe hai')

print('\n Decision tree classes ka use karke yes or no karke feature ko match karta hai  ')

print('\n isme MSE(mean Square Error) ko kam karke kaam karte hai isme overfit zada hota hai  ')

print('\n ')

print('\n ')

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
df = pd.read_csv(r'C:\AKASH\datasets for ml\bangalore.csv')
print(df.head())

X=df.drop('price',axis=1)
y=df['price']
print(X.shape)
print(y.shape)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)#The correct order should have the features (X) first and the target variable (y) second
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)


dtr = DecisionTreeRegressor(criterion='friedman_mse')#criterion ='friedman','mae' aisa boht sare hai check karna jisme achhese baithe vo use karna
dtr.fit(X_train,y_train)
print(dtr.score(X_test,y_test))

#multiple values ko bhi predict kar sakta hai + manual value ko bhi 
print(dtr.predict([X_test.iloc[-1,:]]))
print('actual value',y_test.iloc[-1])


























