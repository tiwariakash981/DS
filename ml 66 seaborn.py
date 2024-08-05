from sklearn.datasets import load_breast_cancer
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cancer_dataset = load_breast_cancer()

cancer_df = pd.DataFrame(np.c_[cancer_dataset['data'],cancer_dataset['target']],
                         columns=np.append(cancer_dataset['feature_names'],['target']))
print(cancer_df)

##sns.pairplot(cancer_df)
##print('scatterplot me sirf do bande ko hi plot kar sakte hai lekin yaha pure dataset ka scatterplot ko lot kar sakte hai')
##plt.show()

##sns.pairplot(cancer_df.vars=['mean radius','mean texture','target'])##vars== used for selecting specific columns
##plt.show()

##sns.pairplot(cancer_df,vars=['mean radius','mean texture',],hue='target')##vars== used for selecting specific columns
##plt.show()

##sns.pairplot(cancer_df,vars=['mean radius','mean texture',],hue='target',pallete='Dark2')##vars== used for selecting specific columns
##plt.show()

#kind check karta hai data linear form me hai ki nhi
sns.pairplot(cancer_df,hue='target',x_vars=['mean radius'],y_vars=['mean texture'],kind='reg',marker='<')##vars== used for selecting specific columns
plt.show()

##we can increase size of pairplot using height parameter 
















