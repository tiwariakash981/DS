import pandas as pd

##ISME currency1 me null values rakha hai handle karne ke liye 
df = pd.read_csv('C:\AKASH\currency1.csv')
print("",df)

df1 = pd.read_csv('C:\AKASH\currency1.csv',na_values='not available')
print("",df1)

df2 = pd.read_csv('C:\AKASH\currency1.csv',na_values={'Symbol':'Null'})
print("ek specific column me change kiya hai bas jaha null hai vaha pe NaN",df2)

df3 = pd.read_csv('C:\AKASH\currency1.csv',keep_default_na=False)
print("jo jaisa rahega vaise print ho jaaega i.e null likha hoga to vaise hhi print ho jaaega",df3)

df4 = pd.read_csv('C:\AKASH\currency1.csv',keep_default_na=True)
print("agar true likha hoga to null ko NaN likh ke dikhaega ",df4)

df5 = pd.read_csv('C:\AKASH\currency1.csv',na_filter=False)
print("Agar file ko as it is print karna hai to false ka use karna",df5)


















