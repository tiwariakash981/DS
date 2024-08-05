import matplotlib.pyplot as plt
import seaborn as sns

tips_df = sns.load_dataset('tips')
print(tips_df)

##hue=sex=do graph dega
sns.set()
kwargs = {'alpha':0.9,'linestyle':':','linewidth':5,'edgecolor':'k'}
sns.barplot(x='day',y='total_bill',hue='sex',data=tips_df,**kwargs)
plt.show()

plt.figure(figsize=(8,4))
sns.barplot(x='day',y='total_bill',hue='sex',data=tips_df,linestyle=':',linewidth=5,edgecolor='k')
plt.savefig('ak5')
plt.show()

ax = sns.barplot(x='day',y='total_bill',hue='sex',data=tips_df,**kwargs)
ax.set(title='Barplot of total_bills',xlabel='days',ylabel='Total Bill')
plt.show()
