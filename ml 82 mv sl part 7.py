import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline 

#Pipelines: Organize and sequence multiple transformations.
#SimpleImputer: Fills missing values using different strategies (mean, median, mode, constant).
#ColumnTransformer: Applies different transformers to different subsets of columns in the dataset.
#Transformer: An object that learns from the data during fit and modifies the data during transform.

#Pipeline ke bare me hai isme aur jaise humlog piche ke tutorials me khudse values ko insert kar rhe the
#lekin isme direct sklearn se karenge
#aur pichle wale sklearn me pure column me value ko daal rhe the
#but isme column ke particular class ke  value me bhi daal sakte hai

train = pd.read_csv(r'C:\AKASH\datasets for ml\house prediction adv regression\train.csv')
test = pd.read_csv(r'C:\AKASH\datasets for ml\house prediction adv regression\test.csv')
print(train.head())
print(test.head())
print(train.shape)
print(test.shape)

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

X_train = train.drop(columns='SalePrice',axis=1)
y_train = train['SalePrice']
X_test = test.copy()

isnull = X_train.isnull().sum()
print(isnull)

num_vars = X_train.select_dtypes(include=['int64','float64'])
cat_vars = X_train.select_dtypes(include=['O'])
print(num_vars.columns)
print(cat_vars.columns)

isnull_num_vars = num_vars.isnull().sum()
isnull_cat_vars = cat_vars.isnull().sum()
##print(isnull_num_vars)
##print(isnull_cat_vars)
mv_num_vars = isnull_num_vars[isnull_num_vars > 0]
mv_cat_vars = isnull_cat_vars[isnull_cat_vars>0]
##print(mv_num_vars)
print(mv_cat_vars)

num_vars_mean = ['LotFrontage']
num_vars_median = ['MasVnrArea','GarageYrBlt']
cat_vars_mode = ['Alley','MasVnrType','BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinType2','Electrical','FireplaceQu']
cat_vars_const = ['GarageType','GarageFinish','GarageQual','GarageCond','PoolQC','Fence','MiscFeature']

mv_num_vars_mean_imputer = Pipeline(steps=[('imputer',SimpleImputer(strategy='mean'))])
mv_num_vars_median_imputer = Pipeline(steps=[('imputer',SimpleImputer(strategy='median'))])
mv_cat_vars_mode_imputer = Pipeline(steps=[('imputer',SimpleImputer(strategy='most_frequent'))])
mv_cat_vars_const_imputer = Pipeline(steps=[('imputer',SimpleImputer(strategy='constant',fill_value='missing'))])

preprocessor = ColumnTransformer(transformers=
            [('mean_imputer',mv_num_vars_mean_imputer,num_vars_mean),
            ('median_imputer',mv_num_vars_median_imputer,num_vars_median),
            ('mode_imputer',mv_cat_vars_mode_imputer,cat_vars_mode),
            ('const_imputer',mv_cat_vars_const_imputer,cat_vars_const)])

print(preprocessor.fit(X_train))
print(preprocessor.transformers)

#ye sklearn ka method hai aur niche ek aur method same check karne ke liye
print(preprocessor.named_transformers_['mean_imputer'].named_steps['imputer'].statistics_)
print(preprocessor.named_transformers_['mode_imputer'].named_steps['imputer'].statistics_)
print(train['LotFrontage'].mean())

X_train_clean = preprocessor.transform(X_train)
X_test_clean = preprocessor.transform(X_test)
print(X_train_clean,X_test_clean)


X_train_clean_miss_var = pd.DataFrame(X_train_clean ,index=X_train.index,
                                      columns = num_vars_mean+num_vars_median+
                                      cat_vars_mode+cat_vars_const)
print(X_train_clean_miss_var.isnull().sum())

print(X_train_clean_miss_var['Alley'])
print(X_train_clean_miss_var['Alley'].value_counts())



#Questions 1.main df jaha mv nhi tha usko bhi add karna hai matlab (add(mv + non-missing value ))
#2.X_test me value fill karna hai

#Answer 1.
nmv_isnull = isnull[isnull == 0].index#nmv=non missing values
df_nmv = X_train[nmv_isnull]
final_df = pd.concat([X_train_clean_miss_var,df_nmv],axis=1)#axis = 1 bolta hai ki columns ko side by side add karo hence it is compulsory
##final_df1 = final_df[X_train.columns]
print('final o/p for complete df',final_df)

























