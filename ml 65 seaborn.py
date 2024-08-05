##Feature Selection aur feature Engeneering me boht kaam aata hai jo feature select karna hai bas vohi karo
##Co relation means ek badha to dusra bhi badhega , corelation ke bare me padhenge yaha

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
##from sklearn.datasets import load_breast_cancer

##gw_df = pd.read_csv(r'C:\AKASH\Who_is_responsible_for_global_warming.csv')
##print(gw_df.head(50))
##
##gw_df = gw_df.drop(columns=['Country Code','Indicator Name','Indicator Code']).set_index('Country Name')
##print(gw_df)
##
###co realation me kuch samajhta nhi hai isliye usko heatmap me daal ke samjhte hai
##print(gw_df.corr())
##
##ax = sns.heatmap(gw_df.corr(),annot=True,linewidth=3)
##ax.tick_params(size=10,color='w',labelsize=10,labelcolor='w')
##plt.title('heatmap') 
##plt.show()
##
##from sklearn.datasets

from sklearn.datasets import load_breast_cancer
cancer_dataset = load_breast_cancer()
##print(cancer_dataset)

cancer_df = pd.DataFrame(np.c_[cancer_dataset['data'],cancer_dataset['target']],
                         columns=np.append(cancer_dataset['feature_names'],['target']))

# Set the display options
##pd.set_option('display.max_rows', None)  # Show all rows
##pd.set_option('display.max_columns', None)  # Show all columns
##pd.set_option('display.max_colwidth', None)  # Show full content of columns
##print(cancer_df)

plt.figure(figsize=(35,35))
ax = sns.heatmap(cancer_df.corr(),annot=True,linewidth=3)
ax.tick_params(size=15,color='w',labelsize=15,labelcolor='k')
plt.title('Heatmap representing Breast Cancer Patients')
plt.show()
