import pandas as pd
a = pd.read_csv(r'C:\AKASH\currency.csv')
print("original data \n",a)

type(a)
print(a.columns)

aa = pd.read_csv(r'C:\AKASH\currency.csv',nrows=5)
##print("printing 5 rows ",aa)

aaa = pd.read_csv(r'C:\AKASH\currency.csv',usecols=[1,2])
##print("printing values of column(1,2) ",aaa)

aaaa = pd.read_csv(r'C:\AKASH\currency.csv',skiprows = 1)
print("skipping first row \n",aaaa)

aaaaab = pd.read_csv(r'C:\AKASH\currency.csv',skiprows = [1])
print("printing rows by using indexing \n",aaaaab)


b = pd.read_csv(r'C:\AKASH\currency.csv',index_col = 2)
print("here 2 represents index value and making heading of index as my 2nd column \n",b)


