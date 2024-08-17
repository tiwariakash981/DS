import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns

df = pd.read_csv(r'C:\AKASH\datasets for ml\house prediction adv regression\train.csv')
print(df.shape)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
##print(df)

#dropping column having greater than 20% NaN values
mv_col_gre_20 = ['Alley','FireplaceQu','PoolQC','Fence','MiscFeature']
df2 = df.drop(columns=mv_col_gre_20)
print(df2.shape)

df3 = df2.select_dtypes(include=['int64','float64'])
print(df3.shape)
##print(df3.isnull().sum())

mv_var = ['LotFrontage','MasVnrArea','GarageYrBlt']
print('knkmin',df3[mv_var][df3[mv_var].isnull().any(axis=1)])

print('LotConfig ke classes(unique values) dikhaega',df['LotConfig'].unique())

#Inside ek class hai i.e unique value
print(df[df.loc[:,'LotConfig']=='Inside'])#vo data jaha bas Inside hoga rows me 
print(df[df.loc[:,'LotConfig']=='Inside']['LotFrontage'])#loc = location

#filling mean value at NaN value
print(df[df.loc[:,'LotConfig']=='Inside']['LotFrontage'].replace(np.NaN,df[df.loc[:,'LotConfig']=='Inside']['LotFrontage'].mean()))

 
df_copy = df.copy()
for var in df['LotConfig'].unique():
    df_copy.update(df[df.loc[:,'LotConfig']==var]['LotFrontage'].replace(np.NaN,df[df.loc[:,'LotConfig']==var]['LotFrontage'].mean()))

print(df_copy.isnull().sum())

cat_vars=['LotConfig','MasVnrType','GarageType']
for cat_var,num_var in zip(cat_vars,mv_var):
    for var_class in df[cat_var].unique():
        df_copy.update(df[df.loc[:,cat_var]==var_class][mv_var].replace(np.nan,df[df.loc[:,cat_var]==var_class][mv_var].mean()))
print('now it will not be updated if cat_var also contain nan values',df_copy[mv_var].isnull().sum())
#hence always check that whether yr cat_var have nan values or not

plot.figure(figsize=(8,4))
sns.set()
for i,var in enumerate(mv_var):
    plot.subplot(2,2,i+1)
    sns.histplot(df[var],bins=20)
    sns.histplot(df_copy[var],bins=20)
##    plt.legend()
plot.show()    


























