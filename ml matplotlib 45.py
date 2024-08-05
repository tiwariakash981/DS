import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import random 

##ml = [rd.randint(1,100) for i in range(50)]
##py = [rd.randint(1,100) for i in range(50)]
##print(ml)
##print(py)

##numpy direct array me store karta hai [] square bracket use karne ki xarurat nhi
ml_std_age = np.random.randint(18,45,(50))
py_std_age = np.random.randint(18,45,(50))
print(ml_std_age)
print(py_std_age)

####rwidth is used for creating different sized bars of a graph
####orientation,histtype
##plt.hist(ml_std_age,bins=[15,20,25,30,35,40,45],rwidth=0.8,histtype='step',
##         orientation='horizontal',color='r',label='ml_std_age') ##it sets range from where to where i have to make design i.e graph
##
##plt.hist(py_std_age,bins=[15,20,25,30,35,40,45],rwidth=0.8,histtype='step',
##         orientation='vertical',color='y',label='ml_std_age')
##
##plt.title('ml student age histogram')
##plt.xlabel('students age category')
##plt.ylabel('no. of students age')
##plt.legend(loc=4)
##plt.show()

##NOTE JO CODE UPAR LIKHA HAI DO BAAR USKO REDUCE KARKE NICHE LIKHA HAI
plt.figure(figsize=(16,9))
style.use('ggplot')
plt.grid(color='r')
plt.hist([ml_std_age,py_std_age],bins=[15,20,25,30,35,40,45],rwidth=0.8,histtype='bar',
         orientation='vertical',color=['r','y'],label=['ml_std_age','py_std_age']) ##it sets range from where to where i have to make design i.e graph

plt.title('ml student age histogram')
plt.xlabel('students age category')
plt.ylabel('no. of students age')
plt.legend(loc=4)
plt.show()
