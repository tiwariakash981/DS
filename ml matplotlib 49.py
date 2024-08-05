import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.style as style



classes = ['Py','R','ML','AI','DS']
class1_std = [45,15,35,25,30]

##plt.pie([3])
##plt.show()

##autopct = har ek value ka actual percentage kitna hai pie chart me vo dikhaega
explode1=[0.06,0,0.06,0,0] ## explode matlab konse point ko normal graph se bahara nikalna hai
colors1 = ['c','m','r','g','b']
textprops1={'fontsize':15}
plt.pie(class1_std,labels=classes,explode=explode1,colors=colors1,
        autopct='%0.2f%%',shadow=True,radius=1.4,startangle=90,textprops=textprops1)##jo angle lega vaha se chalu hoga pie chart banna 
plt.show()









 




























