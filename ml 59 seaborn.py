import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

bins=[0,5,10,15,20,25,30,35,40]
sns.set()
plt.figure(figsize=(8,4))
tips_df = sns.load_dataset('tips')
sns.histplot(tips_df['total_bill'],label='total_bill',bins=bins,hist_kws={'color':'#DC143C'))
sns.histplot(tips_df[''],label='total_bill',bins=bins,hist_kws={'color':'#DC143C')

plt.legend()
plt.show()
print(tips_df.head(50))
print(tips_df.total_bill.sort_values())










