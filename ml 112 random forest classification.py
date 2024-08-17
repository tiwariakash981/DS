print('\n Decision tree ke classification me Gini impurity or entropy ka use karte hai  ')

print('\n Random Forest = Randomly data leke random boht sare decision tree banaenge aur usme se jo zada majority me answer raherga usko select karenge ')

print('\n Main dataset me se random sample lete hai matlab 100 me se 80 rows lenge aur uska prediction karte hai ')

print('\n Classification me majority karte hai aur regression me mean nikal ke o/p dekhenge')

print('\n kitne decision tree use karna hai ye apne upar hai')

print('\n ')

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

print(data.data)
print(data.feature_names)
print(data.target)

df = pd.DataFrame(np.c_[data.data,data.target],columns=[list(data.feature_names)+['target']])
print(df.head())

X=df.iloc[:,0:-1]
y=df.iloc[:,-1]

X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_state=1)
print(X_train.shape)

rfc = RandomForestClassifier(n_estimators=100,criterion='gini')#gini or entropy koi bhi le sakta hu
rfc.fit(X_train,y_train)
print(rfc.score(X_test,y_test))

patient1=np.random.rand(1,30)
patient1 = np.array([patient1])
print(patient1)
rfc.predict(patient1)
print(data.target_names)
pred = rfc.predict(patient1)
print(pred)







