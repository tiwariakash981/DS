import matplotlib.pyplot as plt
##import matplotlib.style as style
from matplotlib import style 

days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
delhi_temp=[36,37,38,39,40,40.1,40.3,42,42.7,40,39,41,42,45,42.9]

mumbai_temp=[36,37,38,39,43,45.1,51.3,47,42.7,39,39,41,42,40,53.9]

##plt.axis is used for setting axis 
##linestyle can be -,--,:
##marker is used for setting some designs at x,y locations
##markersize increases the size of marker

##plt.plot(days,delhi_temp,color='r',marker='o',linestyle=':',linewidth=4,markersize=10)
####plt.axis([0,30,0,50])
##plt.title('Delhi temperature') 
##plt.xlabel('Days')
##plt.ylabel('Temperature')
##plt.show()

##color marker aur linestyle ko ek me bhi likh sakte hai
##plt.plot(days,delhi_temp,'go--',linewidth=4,markersize=10)
##style.use("ggplot")
##plt.grid(color='m',linestyle='-.',linewidth=2) ##grid  style.use kaam nahi kar rha tha isliye ye use kiya
####plt.axis([0,30,0,50])
##plt.title('Mumbai temperature',fontsize=28) ##we can give fontsize
##plt.xlabel('Days')
##plt.ylabel('Temperature')
##plt.legend(['index=temperature'],loc=0) ##label='index=temperature'  ye cheez agar plt.plot wale me likhega to bhi chalega
##plt.show()

plt.plot(days,delhi_temp,'go--',linewidth=4,markersize=10,label='dlehi-temp')
plt.plot(days,mumbai_temp,'yo--',linewidth=4,markersize=10,label='mumbai-temp') ##do this for printing another line

style.use("ggplot")
plt.grid(color='m',linestyle=':',linewidth=2) ##grid  style.use kaam nahi kar rha tha isliye ye use kiya
##plt.axis([0,30,0,50])
plt.title('Delhi & Mumbai temperature',fontsize=28) ##we can give fontsize
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.legend(loc=0) ##label='index=temperature'  ye cheez agar plt.plot wale me likhega to bhi chalega
plt.show()
