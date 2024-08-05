import numpy as np
## Numpy Array Concatination and split
print(" Numpy Array Concatination and split\n")

arr1 = np.arange(1,17).reshape(4,4)
print(arr1)

arr2 = np.arange(17,33).reshape(4,4)
print(arr2)

list1=[1,2,3,4]
list2=[5,6,7,8]
print("adding two lists",list1+list2)

##list normal + symbol use karke concatenate ho jata hai lekin array me concatenate function use karte hai
print("arr1 , arr2 ka concatination:\n ",np.concatenate((arr1,arr2)))
print("arr1 , arr2 ka concatination in horizontal: 1 represents row\n ",np.concatenate((arr1,arr2),axis=1))

print("printing in vertical without using axis ",np.vstack((arr1,arr2)))
print("printing in horizontal without using axis",np.hstack((arr1,arr2)))

list1 = np.split(arr1,2)
print("spliting arrays in two equal halves \n",list1)
print(type(list1))

print("value of list1 0 index :",list1[0])
print("type of 0th index of list1 will be ",type(list1[0]))

print("splitting in row wise and in two equal halves",np.split(arr1,2,axis=1))

d1 = np.arange(1,10)
print(d1)
print("splitting 1d array but showing limited content :",np.split(d1,[1,5]))
