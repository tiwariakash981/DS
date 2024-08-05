import numpy as np
mx = np.array([[[1,1,1],[1,1,1],[1,1,1]]])
print(mx)


##for creating ones array automatically


mx_1s = np.ones((3,3),dtype='int')
print(mx_1s)
print("data type:",mx_1s.dtype)

mx_0s = np.zeros((2,2),dtype='int')
print(mx_0s)

mx_0s = np.zeros((4,6),dtype=str)
print(mx_0s)


##empty string ka boolean value is false aur jab zeroes ko dtype=str dega to empty string aaega 
em_str = ''
print(bool(em_str))

##empty string
em_mx = np.empty((3,3))
print(em_mx)
