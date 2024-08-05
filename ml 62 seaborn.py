import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = sns.load_dataset('titanic')
print('head',titanic_df.head(100))
print('shape = rows vs columns \n',titanic_df.shape)

sns.set()
####hue = ye banda category me divide karta hai data ko , size='who' nhi samjha
##sns.scatterplot(x='age',y='fare',data=titanic_df,hue='sex',style='who',size='who',sizes=(100,400))
##plt.show()

##style = bas har ek category ko alag style or format deta hai
##size=kisko bada chhota karega aur sizes =kitna size dena hai
sns.scatterplot(x='who',y='fare',data=titanic_df,hue='alive',style='alive',size='who',sizes=(100,400))
plt.show()

sns.scatterplot(x='who',y='fare',data=titanic_df,hue='alive',style='alive',size='who',sizes=(100,400))
plt.show()









