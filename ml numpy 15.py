import numpy as np
import matplotlib.pyplot as plt

print("valaue of sin(30)",np.sin(30))
print("value of cos(180)",np.cos(180))

x_sin = np.arange(0,3*np.pi,0.1)
print("value of random x_sin",x_sin)

y_sin = np.sin(x_sin)
print("value of y sin",y_sin)

plt.plot(x_sin,y_sin)
plt.show()

x_cos = np.arange(1,3*np.pi,0.1)
y_cos = np.cos(x_cos)
plt.plot(x_cos,y_cos)
plt.show()
