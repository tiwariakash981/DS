import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import Ridge,Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the cleaned dataset for Bangalore house price prediction
df = pd.read_csv(r'C:\AKASH\datasets for ml\bangalore.csv')  # Bangalore house price prediction ko clean karne ke baad
print(df)

# Separate the features (X) from the target variable (y)
X = df.drop('price', axis=1)
y = df['price']
print(X.shape)  # Print the shape of the features matrix
print(y.shape)  # Print the shape of the target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)

# Standardize the features using StandardScaler
sc = StandardScaler()
sc.fit(X_train)  # Fit the scaler to the training data to learn the scaling parameters
X_train = sc.transform(X_train)  # Apply the scaling to the training data
X_test = sc.transform(X_test)  # Apply the scaling to the testing data
print(X_train)



##Ridge and Lasso Regression
rd = Ridge()
rd.fit(X_train,y_train)
##rd.transform()
print(rd.score(X_test,y_test))

ls = Lasso(alpha=5)#alpha badhane pe thoda accuracy change hota hai
ls.fit(X_train,y_train)
print(ls.score(X_test,y_test))

##rd = Ridge(alpha=2)
##rd.fit(X_train,y_train)
####rd.transform()
##print(rd.score(X_test,y_test))






