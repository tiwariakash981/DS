import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#enumerate dekh niche aur info le

# Load the DataFrame
df = pd.read_csv(r'C:\AKASH\datasets for ml\house prediction adv regression\train.csv')

# Print the first 10 rows as a quick preview (optional)
print(df.head(10))
print('rows vs columns \n', df.shape)

# Set pandas options to display all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Print the entire DataFrame
##print('ye complete data print karega kyuki set_option use kiya hai',df)
# Get and print the current settings
##col = pd.get_option('display.max_columns')
##row = pd.get_option('display.max_rows')
##print(col)
##print(row)


##print('imp hai ye for viewing kaha pr kitna null value hai',df.info())

##print('sare null values ka sum karke dega',df.isnull().sum())

##plt.figure(figsize=(25,25))
##sns.heatmap(df.isnull())
##jaha zada white vaha utna missing values
##plt.show()

null_var = ((df.isnull().sum())/(df.shape[0]) )* (100)
print('jo missing values ka percentage 20% se zada hai usko sidha delete karte hai',null_var)

drop_col = null_var[null_var>15].keys()
print(drop_col)

#now dropping columns
df2 = df.drop(columns=drop_col)
##print(df2.tail())
print(df2.shape)

#isme jaha kuch rows me nan values hai unko drop karenge 
df3 = df2.dropna()
print(df3.tail())
print(df3.shape)

##plt.figure(figsize=(25,25))
##sns.heatmap(df3.isnull())
#jaha zada white vaha utna missing values
##plt.show()

print('it checks for how much NaN values are present ',df3.isnull().sum().sum())

#distplot use kar rhe hai taki pata chale ki apna data cleanning proper hua hai ki nahi 
##print(df3.select_dtypes(include=['int64','float64']).columns)
##sns.histplot(df3['MSSubClass'])
##sns.histplot(df['MSSubClass'])
##plt.show()


num_col = ['MSSubClass', 'LotArea', 'OverallQual', 'OverallCond',
       'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
       'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
       'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
       'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
       'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
       'MoSold', 'YrSold', 'SalePrice']

#zada difference nahi hai matlab data sahi tarike se clean hua hai
##for i,var in enumerate(num_col):
##    plt.subplot(9,4,i+1)
##    sns.histplot(df[var],bins=20)
##    sns.histplot(df3[var],bins=20)
##plt.show()

#ab categorical variables ka graph plot karenge
print(df3.select_dtypes(include='object').columns)

cat_col = ['MSZoning', 'Street', 'LotShape', 'LandContour', 'Utilities',
       'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2',
       'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
       'Exterior2nd', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
       'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Heating',
       'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual', 'Functional',
       'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive',
       'SaleType', 'SaleCondition']

print('ek column me(original df me) kitna data hai uska info hai',df['MSZoning'].value_counts()/df3.shape[0]*100)
print('ek column me kitna data change(df,df3) hua hai uska info',df['MSZoning'].value_counts()/df.shape[0]*100,df3['MSZoning'].value_counts()/df3.shape[0]*100)

#keys use hota hai column naam change karne ke liye
print('ek column me kitna data change(df,df3) hua hai uska info hai ek proper format me ',
      pd.concat([df['MSZoning'].value_counts()/df.shape[0]*100,
      df3['MSZoning'].value_counts()/df3.shape[0]*100],axis=1,keys=['MSZoning org','MSZonning updated']))

def all_cat_col(var):
    return pd.concat([df[var].value_counts()/df.shape[0]*100,
                      df3[var].value_counts()/df3.shape[0]*100],axis=1,keys=[var+'org',var+'updated'])

for var in cat_col :
    print(all_cat_col(var))

print('null',df3.isnull().sum().sum())

##niche wala mwthod use karne pe permanent change ho jata hai lekin ek naya file ban jata hai like train-modified.csv karke usi location pe
df.to_csv(r'C:\AKASH\datasets for ml\house prediction adv regression\train_modified.csv', index=False)
