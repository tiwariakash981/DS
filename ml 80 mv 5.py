import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv(r'C:\AKASH\datasets for ml\house prediction adv regression\train.csv')
print(df.head())

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

cat_var = df.select_dtypes(include='object')# now taking categorical values
print(cat_var)
print(cat_var.shape)

mv_per = cat_var.isnull().mean()*100#dekh yaha sum()/df[column] karne se achha hai mean karde baat vohi padega
print(mv_per)

drop_var = ['Alley','FireplaceQu','PoolQC','Fence','MiscFeature']
##print(df.drop(columns=drop_var,axis=1,inplace=True))
#inplace=True: Modifies the original DataFrame and returns None. The DataFrame is updated in place without needing to assign it back to a variable.
print(cat_var.drop(columns=drop_var,axis=1,inplace=True))#ye wala use karna agar data cleaning karna hai to 
#print(df.columns)

print(cat_var.shape)
#now searching for column with nan values
isnull_per = cat_var.isnull().mean()*100
print(isnull_per)

mv_col = isnull_per[isnull_per>0].keys()
print(mv_col)

cat_var['MasVnrType'].fillna("Missing")
print(cat_var.mode())
print(cat_var.value_counts)

cat_var['MasVnrType'].fillna(cat_var['MasVnrType'].mode()[0])

for var in mv_per:
    cat_var[var].fillna(cat_var[var].mode()[0],inplace=true)
    print(var,"=",cat_var[var].mode()[0])

print(cat_var.isnull().sum())

#histogram use hota hai data ka distribution check karne ke liye heatmap null values check karne ke liye 
for i,var in enumerate(mv_per):
    plt.subplot(4,3,i+1)
    plt.hist(cat_var[var],label='input')
    plt.hist(df[var].dropna(),label='Imput')
plt.show()


df.update(cat_var)
df.drop(columns=drop_var,inplace=True)

df.select_dtype(include='object').isnull().sum()






















