##matplotlib -I
from matplotlib import pyplot as plt ##import matplotlib.pyplot as plt

days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[36,37,38,39,40,40.1,40.3,42,42.7,40,39,41,42,45,42.9]

##plt.axis is used for setting axis 

plt.plot(days,temp)
plt.axis([0,30,0,50])
plt.title('Mumbai temperature')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.show()

