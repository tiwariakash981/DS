import numpy as np

##we will learrn abt some numpy functions 
##arange() it prints numbers from a to b
arr = np.arange(1,13,2)
arr1 = np.arange(1,13)
print("using arange:",arr,arr1)

##linspace() in np used to create random numbers between some numbers
arr = np.linspace(1,4,2)
print("using linspace:",arr)

##reshape() in numpy it changes dimension of array
arr_1d = np.arange(1,13)
arr_2d = arr_1d.reshape(3,4)
arr_3d = arr_1d.reshape(2,3,2) ## Here first element(2=3d),second element(3=2d),third element(2=1d) 
print("2d array using reshape: \n",arr_2d)
print("3d array using reshape:\n",arr_3d)

##ravel() in numpy used for making multidimensional to 1d array
print("converting 3d array into 1d ",arr_3d.ravel())

##flatten() in numpy used for making multidimensional to 1d array
print("converting 2d array into 1d ",arr_2d.flatten())

##transpose() changes from horizontal to vertical and vice versa
print(arr_2d.transpose())















