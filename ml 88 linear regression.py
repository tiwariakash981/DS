#linear regression => y = mx + c ,y=predicted value ,x=actual value which i am giving to model  

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

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
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# Standardize the features using StandardScaler
sc = StandardScaler()
sc.fit(X_train)  # Fit the scaler to the training data to learn the scaling parameters
X_train = sc.transform(X_train)  # Apply the scaling to the training data
X_test = sc.transform(X_test)  # Apply the scaling to the testing data
print(X_train)  # Print the standardized training data

# Initialize and train the Linear Regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Print the coefficients (weights) and intercept learned by the model
print(lr.coef_)  # Coefficient values represent the relationship between features and the target variable
print(lr.intercept_)  # The intercept (bias) term

# Make predictions on the testing data
predictions = lr.predict(X_test)  # Predict the house prices for the test set
print(predictions)

# Evaluate the model's performance using the coefficient of determination (R^2 score)
score = lr.score(X_test, y_test)  # R^2 score measures how well the model predicts the target variable
print(score)
