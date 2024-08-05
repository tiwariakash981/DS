import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as style

classes = ['py','r','ai','ml','ds']
class1_std = [30,10,20,25,10] ##py ke 10 , r ke 10 ... students hai
class2_std = [40,5,20,20,10]
class3_std = [35,5,30,15,15]   

style.use('ggplot')

##plt.figure(figsize=(16,9)) ##increases the size
##plt.bar(classes,class1_std,color='r',width=0.8,align='edge',edgecolor='b'
##        ,linewidth=5,alpha=0.5,linestyle='--',label='class1_std',visible=True)
##plt.title('Bar chart of all coding field',fontsize=10)
##plt.xlabel('fields')
##plt.ylabel('number of students')
##plt.legend()
##plt.show()


##plt.figure(figsize=(16,9)) ##increases the size
##plt.barh(classes,class1_std,color='r',align='edge',edgecolor='b'
##        ,linewidth=2,alpha=0.5,linestyle='--',label='class1_std',visible=True)
##plt.title('Bar chart of all coding field')
##plt.xlabel('fields')
##plt.ylabel('number of students')
##plt.legend()
##plt.show()



##plt.figure(figsize=(16,9)) ##increases the size
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
plt.show()




