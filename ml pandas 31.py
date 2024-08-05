import pandas as pd
##interpolate ke kuch aur parameters it works for numeric data only
##yaad rakhna inplace data ko update kar deta hai
##it means orginal data change hota hai aur baki kai sare me sirf data ka ek copy banta hai


df = pd.read_csv(r'C:\AKASH\numbers.csv')
print('original dataframe\n',df)

print(df.interpolate())

print('checking that there should not be any object daata type',df.dtypes)

print('har ek column me ek value fill hoga',df.interpolate(limit=1))

print('niche side se columns ka value fill hoga ',limit=1,df.interpolate(limit_direction='backward'))
print('upar se columns ka value fill hoga ',limit=2,df.interpolate(limit_direction='forward'))
print('piche se aur aage se columns ka value fill hoga ',limit=2,df.interpolate(limit_direction='both'))

print('andar ke jo values honge data ke vovalid  fill honge  ',df.interpolate(limit_area='inside'))
print('ye nhi samjha mujhe ',df.interpolate(limit_area='outside'))

print('ye banda sidha data update karta hai',inpace=True)








