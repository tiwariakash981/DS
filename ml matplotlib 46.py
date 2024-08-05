import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as style

classes = ['py','r','ai','ml','ds']
class1_std = [30,10,20,25,10] ##py ke 10 , r ke 10 ... students hai
class2_std = [40,5,20,20,10]
class3_std = [35,5,30,15,15]

##visible=False (hides the graph),label=...(graph ke upar content likh ke aaega),alpha=opacity

plt.bar(classes,class1_std,color='r',width=0.2,align='edge',edgecolor='b'
        ,linewidth=5,alpha=0.5,linestyle='--',label='class1_std',visible=False)

plt.legend()
plt.show()
##plt.barh(classes,class3_std)
##plt.show()






