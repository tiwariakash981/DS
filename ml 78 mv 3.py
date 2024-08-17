import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#NOTE: JAB GRAPH NORMAL DISTRIBUTION = SYMMETRIC HO TAB MEAN USE KARNA JAB ASSYMETRIC= SKEWED HO THEN USE MEDIAN FOR FILLING NaN VALUES
#aur uska use tabhi karna jab data randomly NaN ho

##JAB NORMAL DISTRIBUTION HOTA HAI TAB MEAN,MEDIAN,MODE USE KARKE DATA FILL KARO
## ML 78TH VIDEO DEKH ACHHA CONTENT BATAYA HAI GRAPH KE BARE ME 

####BELOW METHOD SHOWS HOW TO LOAD ONLINE DATA BUT  THIS METHOD IS SLOW AND HENCE LOADING FROM OUR SSD

### Convert Google Drive link to direct download link
##file_id = '1B5CHKGPsqDaeRbe8sfWi_Tm6GftSQwo2'
##download_link = f'https://drive.google.com/uc?id={file_id}&export=download'
### Read the CSV file into a DataFrame
##df = pd.read_csv(download_link)
### Print the shape of the DataFrame
##print('Shape of the DataFrame:', df.shape)

df = pd.read_csv(r'C:\AKASH\datasets for ml\house prediction adv regression\train.csv')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
 
##print(df.head())
##print(df.info())
print('df shape:',df.shape)
##print('null\n',df.isnull().sum())
##print(df)

print('null values ',df.isnull().sum().sum())

#mv = missing value
mv_per = df.isnull().sum()/df.shape[0]*100
print(mv_per)

mv_col = mv_per[mv_per > 20 ].keys()
print('it prints mv column name',mv_col)

df2 = df.drop(columns=mv_col)
##print(df2.head())
print('df2 shape:',df2.shape)

#now focusing on numeric data
df3 = df2.select_dtypes(include=['int64','float64'])
print('ak',df3.shape)

##print(df3.isnull().any(axis=1)) #0 = sare column ka naam 1 = rows

##sns.heatmap(df3.isnull())#isme true value ko 1.0 i.e isnull=True otherwise 0.0 (this is for colorbar)
plt.show()

mv_var = [var for var in df3.columns if df[var].isnull().sum()>0]
print('columns which have NaN values:',mv_var)
##for i,var in enumerate(mv_var):
##    plt.subplot(2,2,i+1)
##    sns.histplot(df3[var],bins=20,kde_kws={'linewidth':5,'color':'r'})
##plt.show()


df4 = df3.fillna(df3.mean())
print('checking for NaN values',df4.isnull().sum().sum())

#isme error aa rha hai check kar 
##sns.set()
##for i,var in enumerate(mv_var):
##    plt.subplot(2,2,i+1)
##    sns.histplot(df3[var],bins=20,kde_kws={'linewidth':8,'color':'g'},label='original')
##    sns.histplot(df4[var],bins=20,kde_kws={'linewidth':5,'color':'b'},label='updated')
##    plt.legend()
##plt.show()
 
df5 = df3.fillna(df3.median())
##sns.set()
##for i,var in enumerate(mv_var):
##    plt.subplot(2,2,i+1)
##    sns.histplot(df3[var],bins=20,kde_kws={'linewidth':8,'color':'g'},label='original')
##    sns.histplot(df4[var],bins=20,kde_kws={'linewidth':5,'color':'b'},label='updated')
##    sns.histplot(df5[var],bins=20,kde_kws={'linewidth':5,'color':'b'},label='updated')
##    plt.legend()
##plt.show()

##for i,var in enumerate(mv_var):
##    plt.figure(figsize=(10,10))
##    plt.subplot(3,1,1)
##    sns.boxplot(df[var])
##    plt.subplot(3,1,2)
##    sns.boxplot(df4[var])
##    plt.subplot(3,1,3)
##    sns.boxplot(df5[var])
##    plt.show()
    
df_concat = pd.concat([df3[mv_var],df4[mv_var],df5[mv_var]])
print(df_concat)
print(df_concat[df_concat.isnull().any(axis=1)])
##df3 = df2.dropna()#yaad rakhna yaha original df mat use karna df2 use karna nhi to pura df hi drop ho jaaega
##print('df3 shape: ',df3.shape)
##print(df3)






