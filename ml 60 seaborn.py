import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

##NOTE : NUMERIC DATA = total_bill , CATEGORICAL DATA = DAYS = DATA WHICH CAN BE DIVIDED IN CATEGORIES

tips_df = sns.load_dataset('tips')
print(tips_df.head(90))

##sns.barplot(x=tips_df.day,y=tips_df.total_bill)
##plt.show()
##
##sns.barplot(x=tips_df.day,y=tips_df.total_bill,hue=tips_df.sex)
####sns.barplot(x='day',y='total_bill',hue='sex',data=tips_df) another way for writing content
##plt.show()

####days of week ka order set kar rha hai
##order=['Sun','Thur','Fri','Sat']
##sns.barplot(x=tips_df.day,y=tips_df.total_bill,hue=tips_df.sex,order=order)
##plt.show()

####male aur female  ka order set kar rhe hai
##hue_order = ['Female','Male']
##sns.barplot(x=tips_df.day,y=tips_df.total_bill,hue=tips_df.sex,order=order,hue_order=hue_order)
##plt.show()

####mean ke liye code likh rahe hai
##sns.barplot(x=tips_df.day,y=tips_df.total_bill,hue=tips_df.sex,estimator=np.mean)
##plt.show()

####jo black line aa rha hai usko kam karne ke liye code
##sns.barplot(x=tips_df.day,y=tips_df.total_bill,hue=tips_df.sex,ci=2)
##plt.show()

####categorical data ko y pe rakh aur numeric data ko x pe tab graph horizaontal me change ho jaaega 
##sns.barplot(y=tips_df.day,x=tips_df.total_bill,hue=tips_df.sex,)
##plt.show()

##for both numeric data use orient='h' for changing orientation
sns.barplot(x='total_bill',y='size',orient='h',data=tips_df,hue='sex',color='r',saturation=0.8)
plt.show()

sns.barplot(x='total_bill',y='size',orient='h',data=tips_df,hue='sex',color='r',saturation=0.8)
plt.show()




