##ye wale video me pata chalega ki score ka matlab kya hota hai in short zada score matlab actual data ke aas paas ki value mil rahi hai apne ko aur uska ek formula hota hai usko bhi dekh gpt pe search kar 

#error ko cost function bolte hai
#error isliye nikalte hai taki pata chale ki apna model best hai ya nahi
#error 0,0.1,0.2..... aisa kuch aa raha hai to usko humlog overfit bolenge matlab jo apna model hi usne error ko memorise kar liya hai

#model evaluation is essential step in ml
#error zada ho to phirse data preprocessing kar aur uske baad bhi error ho to model change kar

#residual = y - y^ residual=error (jitna kam utna achha model)
#r square ek measure hai jo batata hai kitna paas me line draw hua hai tere data ke paas
#Goodness of fit matlab error kam hai aur actual,predicted value are close to each other
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import Ridge,Lasso,LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error,r2_score

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
X_train_sc = sc.transform(X_train)  # Apply the scaling to the training data
X_test_sc = sc.transform(X_test)  # Apply the scaling to the testing data
print(X_train_sc)
print(X_test_sc)

lr = LinearRegression()
lr.fit(X_train,y_train)
##lr.transform(X_train)
print('actual value',y_test)
y_pred = lr.predict(X_test)
print('predicted value',y_pred)
print(lr.score(X_test,y_test))


mse = mean_squared_error(y_test,y_pred)
rmse = np.sqrt(mse)
print('ye error bata raha hai ki kitne lakh ka error hai','mse = ',mse,'rmse = ',rmse)

print(r2_score(y_test,y_pred))



 
