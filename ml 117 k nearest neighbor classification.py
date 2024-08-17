#k nearest neighbor 

import pickle,joblib 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier

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

k = KNeighborsClassifier(n_neighbors=5)
k.fit(X_train,y_train)
print(k.score(X_test,y_test))

#for particular value check
patient1=np.random.rand(1,30)
patient1 = np.array([patient1])
pred = k.predict(patient1)
print(pred)

if pred[0]==0:
    print('patient has cancer(malignant)')
else:
    print('no cancer ')

##
##print(pickle.dump(rfc,open('rfc_model','wb')))#ye mere Data Science wale me save ho jaaega 
##
##model_check = pickle.load(open('rfc_model','rb'))
##print(model_check.predict(X_test))
##print('0 means patient has cancer melignain tumour  ')
##
##joblib.dump(rfc,'rfc_model2')
##model_check2 = joblib.load('rfc_model')
##print(model_check2.predict(X_test))
##
##
##
##
##
##
##






























