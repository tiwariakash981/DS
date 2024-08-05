##heatmap is mainly used for feature engeneering seaborn part 10
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gw_df = pd.read_csv(r'C:\AKASH\Who_is_responsible_for_global_warming.csv')
print(gw_df.head(10))

gw_df = gw_df.drop(columns=['Country Code','Indicator Name','Indicator Code']).set_index('Country Name')
print(gw_df)

##annot = real values , cmap = color filter ,color:font color of annot value,back color= text ke background ka color
annot_kws1 = {'fontsize':10,'fontstyle':'italic','color':'w','rotation':'vertical','backgroundcolor':'k'}
cbar_kws={}
sns.heatmap(gw_df,cmap='coolwarm',annot=True,annot_kws=annot_kws1,linewidth=4,cbar=False,xticklabels=False,yticklabels=False)
plt.show()


##cbar = color bar ko bhi change kar sakte hai vo nhi kiya hu online dekh lena
##mai ytick aur xtick label ko bhi change kar sakta hu agar chahiye to
##ml 63 seaborn me thoda boht ax.set() aisa kuch likha hu vo bhi dekh lena ek baar
##sns.set(font_Scale=5) isko use karke x,y ka fontsize change kar sakta hai



