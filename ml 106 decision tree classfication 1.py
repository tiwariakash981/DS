print('\nSupervised learning ke liye Decision tree ko use karte hai')

print('\nWhat is Gini Impurity and entropy')

print('\nsklearn ka CART algorithm use kar ke Decision tree kam karta hai')

print('\n decision tree data ko split karta hai')

print('\n melignant matlab cancer hai matlab 0 se represent hoga nahi to nahi hai')

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = load_breast_cancer()
print(data.data)
print(data.feature_names)
print(data.target)


df = pd.DataFrame(np.c_[data.data,data.target],columns=[list(data.feature_names)+['target']])
print(df.head())
print(df.shape)

#define X,y
X=df.iloc[:,0:-1]
y=df.iloc[:,-1]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=21)
print(X_train.shape)
print(X_test.shape)


#isme feature scale kiya hua data de chahe na de zada koi impact nhi padega
dt = DecisionTreeClassifier(criterion='gini')#criterion='entropy' bhi le sakte hai
dt.fit(X_train,y_train)
##dt.transform(X_train)
print(dt.score(X_test,y_test))

#manually bhi data deke check kar sakta hu ki breast cancer hai ki nhi
#patient1=[yaha pe 30 features ka list de ]
#patient1=np.array([patient1])
#dt.predict(patient1)















