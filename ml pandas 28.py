import pandas as pd
##fillna(),ffill,bfill,limit,inplace
df = pd.read_csv(r"C:\AKASH\currency1.csv")
print(df)

print("NaN values ke jagah '2' likh ke aa jaaega\n", df.fillna(2))
print("NaN values ke jagah column me jo likhega vo aa jaaega\n", df.fillna({'Code': 'done', 'Date': 5}))

print("NaN values ke piche jo value hoga vo aage tak bhar jaaega \n", df.ffill)
print("NaN values ke aage jo value hoga vo piche tak bhar jaaega \n", df.bfill)

print("particular column me particular value daal sakte hai", df.fillna({'Code': 'try1', 'Date': 'try2'}))

print("ye sirf ek value ko '1' likhega har column me",df.fillna(1,limit=1))
print("ye 4 jagah pe '1' likhega har column me",df.fillna( 1, limit=4))

print("ffill na data ko update kar deta hai to yaad rakhna ki original data chahiye rahega to iske upar code likhna", df.ffill( limit=2))

print("ak",df.fillna(5,inplace=True))
