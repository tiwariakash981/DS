import pandas as pd

df = pd.read_csv("C:\\AKASH\\currency1.csv")
print(df)

print("0=row,1=column jaha pe null value hoga column me vo column hat jaaega",df.dropna(axis=1))
print("0=row,1=column jaha pe null value hoga row me vo row hat jaaega",df.dropna(axis=0))

print("mk",df.dropna(how='any'))

print("ye kam se kam ek notnull value ko print karega",df.dropna(thresh=1))
print("ye kam se kam 4 notnull value ko print karega",df.dropna(thresh=4))

print("jis column me NaN value hoga us column ke drop values ko drop kar dega\n ",df.dropna(subset=['Code']))

print("NaN values ko drop karke update krega",df.dropna(inplace=True))




