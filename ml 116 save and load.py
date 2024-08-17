print('\n Serialization is a process of saving our model  ')

print('\n yaha model save karne ka tarika bataya hai ')

print('\n joblib zada achha hai large no. of model ko save karne ke liye  ')

print('\n file binary format me save hota hai ')

print('\n Data ko dump karke uska permanently save karte hai taki  baar baar calculations na karna pade ')

print('\n ')

import pickle,joblib 
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


print(pickle.dump(rfc,open('rfc_model','wb')))#ye mere Data Science wale me save ho jaaega 

model_check = pickle.load(open('rfc_model','rb'))
print(model_check.predict(X_test))
print('0 means patient has cancer melignain tumour  ')

joblib.dump(rfc,'rfc_model2')
model_check2 = joblib.load('rfc_model')
print(model_check2.predict(X_test))


























