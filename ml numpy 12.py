import numpy as np
arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(1,10).reshape(3,3)

print("matrix1 :",arr1)
print("matrix2 :",arr2)

print("manual addition of two matrix", arr1+arr2)
print(np.add(arr1,arr2))

print("manual subtraction using arr1-arr2:",arr1-arr2)
print("subtraction using np.subtract:",np.subtract(arr1,arr2))

print("division using arr1/arr2 :",arr1/arr2)
print("division using np.divide():",np.divide(arr1,arr2))

print("ye normal(elementary) multiplication hai python me:",arr1*arr2)
print("normal multiplication using np.multiply:",np.multiply(arr1,arr2))

print("matrix multiplication using @:",arr1@arr2)
print("matrix multiplication using function dot():\n",np.dot(arr1,arr2))

## finding maximum value of any array can do same for minimum
print("maximum value of arr1:",arr1.max())
print("finding index no. using np.argmax() function:",arr1.argmax())

##max value in a column or row where column = 0 , row = 1
print("0 represents column means highest values for columns are:",arr1.max(axis=0))
print("1 represents row means highest values for row are:",arr1.max(axis=1))

##min value in a column or row where column = 0 , row = 1
print("0 represents column means highest values for columns are:",arr1.min(axis=0))
print("1 represents row means highest values for row are:",arr1.min(axis=1))

##sum of a single matrix or of a single column
print("sum of a single array",np.sum(arr1))
print("it gives sum of each column",np.sum(arr1,axis=0))

##calculating mean
print("mean value of an array",np.mean(arr1))

##calculating squareroot
print("square root value of an array",np.sqrt(arr1))

##calculating standard deviation
print("standard deviation value of an array",np.std(arr1))


##exponential value finding
print("exponential value of arr1 :",np.exp(arr1))


##calculating natural log
print("log of arr1:",np.log(arr1))
print("calculating k log ",np.log10(arr1))##k=10
 




















