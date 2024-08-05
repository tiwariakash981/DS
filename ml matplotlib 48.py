import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.style as style

df = pd.read_csv(r'C:\AKASH\archive data for ml data science\googleplaystore.csv',nrows=1000)
print(df)

print('rows aur columns ka info dega',df.shape)
x=df['Rating']
y=df['Reviews']
y1=df['Installs']
## we can use alpha also as alpha=1 in plt.plot
plt.scatter(x,y,color='r',marker='+',s=50,linewidths=1)
plt.title('Ratings vs Reviews',fontsize=15)
plt.xlabel('Rating')
plt.ylabel('Reviews')
plt.show()


plt.scatter(x,y1,color='r',marker='*',s=50,linewidths=1)
plt.title('Ratings vs Reviews',fontsize=15)
plt.xlabel('Rating')
plt.ylabel('Reviews')
plt.show()



















