# melignain matlab breast cancer hua hai
import numpy as np
import pandas as pd
##from sklearn.metrics import
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data = load_breast_cancer()
print('ye data ko show karega',data.data)
print('for knowing column names',data.feature_names)
print('ye target variable ka content dikhaega',data.target)

df = pd.DataFrame(np.c_[data.data,data.target],columns = [list(data.feature_names)+['target']])
print(df.head())
print(df.shape) 

X=df.iloc[:,0:-1]
y=df.iloc[:,-1]
print('X,y shape',X.shape,y.shape)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#SVC support vector classifier
svc_rbf = SVC(kernel='rbf')
svc_rbf.fit(X_train,y_train)
print('without feature scaling',svc_rbf.score(X_test,y_test))

#Feature scaling
#y_train is a categorical variable, not a continuous
#numerical feature. It represents classes (e.g., 0 for benign and 1 for malignant) 
sc = StandardScaler()
sc.fit(X_train)
X_train_sc = sc.transform(X_train)
X_test_sc = sc.transform(X_test)


svc_rbf2 = SVC(kernel='rbf')
svc_rbf2.fit(X_train_sc,y_train)
print('with feature scaling',svc_rbf2 .score(X_test_sc,y_test))


#now polynomial classifier
svc_poly = SVC(kernel='poly',degree=2)
svc_poly.fit(X_train_sc,y_train)
svc_poly.transform(X_train_sc,y_train)
print(svc_poly.score(X_test,y_test))

#svc linear
svc_linear = SVC(kernel='linear')
svc_linear.fit()
print('jitna bhi kernel trick hai vo sab khudse use kar sakta hai ')















