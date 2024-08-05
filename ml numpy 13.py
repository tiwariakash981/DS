import numpy as np
mx = np.arange(1,101).reshape(10,10)
print(mx)
print("printing matrix",mx[:])
print("printing the row",mx[0])
print("printing column in 1d ",mx[:,0])

print("printing 0,0 element",mx[0,0])
print("printing dimension of 0,1th value",mx[0,1].ndim)
print("printing dimension of 0,0th value",mx[0,0].ndim)

print("printing columns in 2d from a to b ",mx[:,0:1])
print("printing dimension af above column ",mx[:,0:1].ndim)

print("printing specific matrix \n",mx[1:4,1:4])
print("printing more than one columns \n",mx[:,1:4])

print("space required to store this matrix in byte",mx.itemsize)
print("print data type i.e how it is stored in the memory",mx.dtype)
