import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer #import sklearn.impute # I can import whole module , SimpleImputer is just a class 

##X_train me 'X' capital isliye rehta hai kyuki ye matrix ko represent karta hai  aur y_train me 'y' vector ko represent karta hai

train = pd.read_csv(r'C:\AKASH\datasets for ml\house prediction adv regression\train.csv')
test  = pd.read_csv(r'C:\AKASH\datasets for ml\house prediction adv regression\test.csv')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

#train = jiska use karke model train karega , test = jiska use karke last me test karega tere model ko
print('shape of train',train.shape)
print('shape of testt',test.shape)

#It is known as separating features and targets
X_train = train.drop(columns='SalePrice')
y_train = train['SalePrice'] #SalePrice apna target variable hai
print('shape of train',X_train.shape)
print('shape of testt',y_train.shape)

num_vars = X_train.select_dtypes(include=['int64','float64']).columns
cat_vars = X_train.select_dtypes(include=['O']).columns#for object based columns
print('numerical variable:\n',num_vars,'\ncat_vars :\n',cat_vars)
print(X_train[num_vars].isnull().sum())

imputer_mean = SimpleImputer(strategy='mean') #yaha object bana diya
imputer_self = SimpleImputer(strategy='constant',fill_value=1)#for filling manual values
imputer_mean.fit(X_train[num_vars])#yaha par imputer.mean ne Xx_train ke andar num_vars ke sare columns ka mean value nikal ke rakh liya hai
print('values of median',imputer_mean.statistics_)#ye bataega ki median value kya hai

##print('so now adding values ',imputer_mean.transform(X_train[num_vars]))
#jo value train me diya hai vohi test me bhi dede kyuki baad me test value me aur kuch nan value aaya to dikkat nahi hona chahe model me 
X_train[num_vars] = imputer_mean.transform(X_train[num_vars])
test[num_vars] = imputer_mean.transform(test[num_vars])

print(X_train[num_vars].isnull().sum())
print(test[num_vars].isnull().sum())

##Now programming for cat_var
print('x_train columns containing null values',X_train[cat_vars].isnull().sum())
imputer_mode = SimpleImputer(strategy='most_frequent')#mode ke liye most_frequent use karte hai
imputer_mode.fit(X_train[cat_vars])
X_train[cat_vars] = imputer_mode.transform(X_train[cat_vars])
print('checkking the expected values',imputer_mode.statistics_)
test[cat_vars] = imputer_mode.transform(test[cat_vars])

print(X_train[cat_vars].isnull().sum())
print(test[cat_vars].isnull().sum())




