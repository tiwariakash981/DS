import pandas as pd
##"ye isliye kyuki future me python ka update aaega aur regex wale me kuch na kuch change hoga ",
pd.set_option('future.no_silent_downcasting', True)

df = pd.read_csv(r'C:\AKASH\currency.csv')
print(df)

print("using replace function only works in data not in column \n",df.replace('AED','Cod'))
print("multiple values replced with single word and can also do vice versa",df.replace(['ZAR','ZMW'],'updated_value'))

print("column ke andar ke specific content ko change kiya hu",df.replace({'Code':'ZMW'},'none'))

print("replacing using regex",df.replace('[A-Za-z]',0,regex=True))

print("replacing in columns only",df.replace({'Code': '[A-Za-z]'}, {'Code': 0}, regex=True))

print(df.replace('ZMW',method='ffill'))

print("bfill use hoga aur sirf 2 value hi replace hoga ",df.replace(0,method='bfill',limit=2))

print("inplace use karega to data update ho jata hai direct ye yaad rakhna kaam ki  baat hai ",df.replace('ZMW','update',inplace=True) )




