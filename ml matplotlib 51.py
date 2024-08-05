## Subplot 
import matplotlib.pyplot as plt
import random
import matplotlib.style as style
import pandas as pd
import numpy as np

##plt.subplot(2,2,1)
##plt.pie([1])
##
##plt.subplot(2,2,2)
##plt.pie([1,2])
##
##plt.subplot(2,2,3)
##plt.pie([1,2,3])
##
##plt.subplot(2,2,4)
##plt.pie([1,2,3,4])
##plt.show()

plt.figure(figsize=(8,4))

plt.subplot(3,2,1)##row,column,index
days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[36,37,38,39,40,40.1,40.3,42,42.7,40,39,41,42,45,42.9]
##plt.axis is used for setting axis 
plt.plot(days,temp)
##plt.axis([0,30,0,50])
plt.title('Mumbai temperature')
plt.xlabel('Days')
plt.ylabel('Temperature')


plt.subplot(3,2,2)
days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
delhi_temp=[36,37,38,39,40,40.1,40.3,42,42.7,40,39,41,42,45,42.9]
mumbai_temp=[36,37,38,39,43,45.1,51.3,47,42.7,39,39,41,42,40,53.9]
plt.plot(days,delhi_temp,'go--',linewidth=4,markersize=10,label='dlehi-temp')
plt.plot(days,mumbai_temp,'yo--',linewidth=4,markersize=10,label='mumbai-temp') ##do this for printing another line
style.use("ggplot")
plt.grid(color='m',linestyle=':',linewidth=2) ##grid  style.use kaam nahi kar rha tha isliye ye use kiya
##plt.axis([0,30,0,50])
plt.title('Delhi & Mumbai temperature',fontsize=28) ##we can give fontsize
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.legend(loc=0) ##label='index=temperature'  ye cheez agar plt.plot wale me likhega to bhi chalega


plt.subplot(3,2,3)
ml_std_age = np.random.randint(18,45,(50))
py_std_age = np.random.randint(18,45,(50))
style.use('ggplot')
plt.grid(color='r')
plt.hist([ml_std_age,py_std_age],bins=[15,20,25,30,35,40,45],rwidth=0.8,histtype='bar',
         orientation='vertical',color=['r','y'],label=['ml_std_age','py_std_age']) ##it sets range from where to where i have to make design i.e graph

plt.title('ml student age histogram')
plt.xlabel('students age category')
plt.ylabel('no. of students age')
plt.legend(loc=4)


plt.subplot(3,2,4)
classes = ['py','r','ai','ml','ds']
class1_std = [30,10,20,25,10] ##py ke 10 , r ke 10 ... students hai
class2_std = [40,5,20,20,10]
class3_std = [35,5,30,15,15]
width = 0.2
classes_index = np.arange(len(classes))
plt.bar(classes_index,class1_std,width,color='r',label='class1_std')
plt.bar(classes_index + width,class2_std,width,color='g',label='class2_std')
plt.bar(classes_index + width + width,class3_std,width,color='b',label='class3_std')
plt.xticks(classes_index,classes,rotation=45)##graph ke niche python,r,... ye sab likh ke nahi aa rha tha isliye ye use kiya
plt.title('Bar chart of all coding field',fontsize=10)
plt.xlabel('fields')
plt.ylabel('number of students')
plt.legend()


plt.subplot(3,2,5)

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


plt.subplot(3,2,6,projection='polar',frameon=True)##frameon = subplot show nahi hoga,projection = polar = circle me ek 
plt.show()
