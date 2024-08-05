## pivot is specially for numeric 

import pandas as pd

# Read the CSV file
df1 = pd.read_csv(r'C:\AKASH\numbers.csv')

# Print the dataframe
print(df1)

##NOTE : BYDEFAULT YE MEAN VALUES DETA HAI
# Create a pivot table, specifying the numeric columns to aggregate
pivot = df1.pivot_table(index='n1', values=['n3', 'n4'], aggfunc='mean')

# Print the pivot table
print(pivot)

##aggfunc me sum , max , min ye sab use kar sakta hai

print(df1.pivot_table(index='n1', values=['n3', 'n4'], aggfunc='mean',fill_value=0))
print('yaha pe all karke ek column aaega jo bataega kitna sum hua hai',df1.pivot_table(index='n1', values=['n3', 'n4'], aggfunc='mean',fill_value=0,margins=True))
