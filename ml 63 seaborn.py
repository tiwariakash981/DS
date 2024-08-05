import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

arr_2d = np.linspace(1,5,12).reshape(4,3)##rows and then columns
print(arr_2d)
sns.heatmap(arr_2d)
plt.show()

df = pd.read_csv(r'C:\AKASH\currency1.csv')
print(df)

gw_df = pd.read_csv(r'C:\AKASH\Who_is_responsible_for_global_warming.csv')
print(gw_df)

gw_df = gw_df.drop(columns=['Country Code','Indicator Name','Indicator Code'],axis=1).set_index('Country Name')
print(gw_df.head(50))

##cmap assigns color , annot == actual value bhi dene lagta hai 
sns.heatmap(gw_df,vmin=0,vmax=21,cmap='coolwarm',annot=True)
plt.show()

##agar value change karne ka hai actual value ke jagah to ye karne ka

annot_arr = np.array([['a00','a01','a02'],['a10','a11','a12'],['a20','a21','a22'],['a30','a31','a32']])
print(annot_arr)

##fmt ko batana padta hai konse type ka datatype hai ye
sns.heatmap(arr_2d,annot=annot_arr,fmt='s')
plt.show()

