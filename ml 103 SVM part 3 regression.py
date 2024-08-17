#SVM ka kernel='linear 'aur linear regression lagbhag same hai 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler  
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

df = pd.read_csv(r'C:\AKASH\datasets for ml\bangalore.csv')
print(df.head())
print(df.shape)

X = df.drop('price',axis=1)
y = df['price']
print(X.shape)
print(y.shape)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=51)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#Feature Scaling
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)
print(X_train.shape)
print(X_train)

#using SVR(support vector regression)
svr_rbf = SVR(kernel='rbf')
svr_rbf.fit(X_train,y_train)
print(svr_rbf.score(X_test,y_test))

svr_linear = SVR(kernel='linear')
svr_linear.fit(X_train,y_train)
print(svr_linear.score(X_test,y_test))

svr_poly = SVR(kernel='poly',degree=2)
svr_poly.fit(X_train,y_train)
print(svr_poly.score(X_test,y_test))

##print(svr_linear.predict(X_test[0]).reshape(1,1))
y_pred = svr_linear.predict(X_test)
print(y_pred)


#calculating root mean square error
mse = mean_squared_error(y_test,y_pred)
rmse = np.sqrt(mse)
print('63 lakh ka farak aa rha hai original data se boht zada hai ye',rmse)

































