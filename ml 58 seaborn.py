import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

tips_df = sns.load_dataset('tips')
sns.displot(tips_df['size'])##can use displot or histplot
plt.show()

##y=tips_df for horizontal
sns.histplot(y=tips_df['size'],bins=[0,1,2,3,4,5,6,7,8],color='r',label='ak')##bins=100=there will be 100 lines 
plt.legend()##label='ak' ke liye legend() use kiye
plt.title('Done')
plt.show()




