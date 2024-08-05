import pandas as pd

a = pd.read_csv(r'C:\AKASH\currency.csv')
print("original data \n",a)

b = pd.read_csv(r'C:\AKASH\currency.csv',header=1)
print("it is similar to skiprow but here your row becomes yr header(based on index number)\n ",b)

c = pd.read_csv(r'C:\AKASH\currency.csv',header=None)
print("agar header nahi dikhana ho to ye kar sakta hai \n",c)

##isme error aa rha hai
##d = pd.read_csv(r'C:\AKASH\currency.csv',header=None,prefix='Columns')
##print("agar header nahi dikhana ho aur kuch header ke jagah likhna ho to to ye kar sakta hai \n",d)


e = pd.read_csv(r'C:\AKASH\currency.csv',names=['a','b','c'])
print("agar heading ko value dena hai to name function ka use kar \n",e)












