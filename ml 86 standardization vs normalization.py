import  numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#feature scaling ml ka last step hai iske baad ml ke model banate hai
#it  is done on numerical variables 
df = sns.load_dataset('titanic')
print(df.head())

#ye independent variables hai'pclass','age','parch' survived dependent  variable hai aur ye baki teeno pe depend hai 
df2 = df[['survived','pclass','age','parch']]#survivved apna target feature hai
df3 = df2.fillna(df2.mean())
print(df2.head())

#Matrix me independent variable ko rakhte hai. Here X_train comes (not fully confirmed) 
#vector me dependent variable. Here target variable comes i.e y_train(not fully confirmed)

X = df3.drop('survived',axis=1)
y = df3['survived']
print('shape of x ',X.shape)
print('shape of y ',y.shape)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=51)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

sc = StandardScaler()#train data me se mean aur standard deviation value ko train aur learn karega
sc.fit(X_train)
print(sc.mean_)#checks for mean value 
print(sc.scale_)#checks for std_deviation
print(X_train.describe())#ye sare cheezo ko describe karega

#we Don't need to scale dependent variable
X_train_sc = sc.transform(X_train)
X_test_sc = sc.transform(X_test)
print(X_train_sc)

X_train_sc = pd.DataFrame(X_test_sc,columns=['pclass','age','parch'])
X_test_sc = pd.DataFrame(X_test_sc,columns=['pclass','age','parch'])
print(X_train_sc)
print(X_test_sc)

print(X_train_sc.describe())
print(X_train_sc.describe()).round(2)


mmc =MinMaxScaler()
mmc.fit(X_train)

X_train_mmc = mmc.transform(_train)
X_test_mmc = mmc.transform(_train)
print(X_train_mmc)

X_train_mmc = pd.DataFrame(X_train_mmc,columns=['pclass','age','parch'])
X_test_mmc = pd.DataFrame(X_train_mmc,columns=['pclass','age','parch'])
print(X_test_mmc.describe())

sns.pairplot(X_train)
plt.show()

sns.pairplot(X_train)
plt.show()





































