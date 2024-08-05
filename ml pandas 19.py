import pandas as pd
print(pd.__version__)

lists = [1,2,3,"ak",-123]
print(lists)

series1 = pd.Series(lists)
print("printing series by using a list",series1)
print("printing type of series",type(series1))

series2 = pd.Series([1,2,3,4])
print("printing series",series2)

empty_s = pd.Series([])
print("creating empty seriies",empty_s)

series3 = pd.Series([1,4,3,6],index=['a','b','c','d'],dtype=float)
print("printing series, assigning index values ",series3)

series4 = pd.Series([1,2,4],index=['a','b','c'],dtype=float,name="data values")
print("series creation, assigning names, changing data type ",series4)

scalar_series = pd.Series(0.5,index=[0,1,2,3])
print("creating series using a single value and multiple  index ",scalar_series)

dict_s =pd.Series({'a':1,'b':2})
print("creating series using dictionary",dict_s)

##using series2 for slicing
print("value at 0th index :",series2[0])
print("printing values from 0 to nth index",series2[0:])
print("max value:",max(series2))
print("min value:",min(series2))

##can perform conditional operators
print("printing value greater than 2 from series2\n",series2[series2>2])

##we can perform any maths operation
print("adding two equal series",series2+series3)
print("adding unequal series",series3+series4)





