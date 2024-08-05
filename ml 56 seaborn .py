import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

##seaborn data ko dataFrame me leta hai

days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[36,3,37,37.7,39,40.1,43,45,45.6,40.1,44,45,46,47,47.6]
print(len(temp))
temp_df = pd.DataFrame({'Days':days,'Temp':temp})
sns.lineplot(x='Days',y='Temp',data=temp_df)##isme x='days' ye ek label hai aur data = temp_df x,y ka value de rha hai for plotting graph
plt.show()

##another method 
##import seaborn as sns
##import matplotlib.pyplot as plt
##days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
##temp = [36, 3, 37, 37.7, 39, 40.1, 43, 45, 45.6, 40.1, 44, 45, 46, 47, 47.6]
##sns.lineplot(x=days, y=temp)
##plt.show()


tips_df = sns.load_dataset('tips')##it's already downloaded while installing seaborn
print(tips_df.head(50))
print('rows vs columns',tips_df.shape)

sns.lineplot(x='total_bill',y='tip',data=tips_df)
plt.show()

sns.lineplot(x='size',y='total_bill',data=tips_df)
plt.show()
















