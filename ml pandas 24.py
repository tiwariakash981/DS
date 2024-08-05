import pandas as pd

a = pd.read_csv('C:\AKASH\currency.csv')
print("\n",a)

print("bydefault it prints 5 values from head\n",a.head())
print("bydefault it prints 5 values from last\n",a.tail())
print("it prints 2  values from last\n",a.tail(2))

b = pd.read_csv('C:\AKASH\currency.csv',dtype={'Name':'string'})
print("here we can change datatype \n",b)

c = pd.read_csv('C:\AKASH\currency.csv',true_values=['yes'])
print("converts yes keyword to 'True'",c)

d = pd.read_csv('C:\AKASH\currency.csv',false_values=['No'])
print("it writes False where there will be 'No' written in our data ",d)






