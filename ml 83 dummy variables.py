import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Set display options to show all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Read the CSV file into a DataFrame
tips_df = pd.read_csv(r'C:\AKASH\datasets for ml\tips.csv',header=1)
tips_df = tips_df.iloc[:,:7]
print(tips_df)

dummy_df = pd.get_dummies(tips_df)
print(dummy_df)

#drop_first = sex_male,sex_female ke column me koi ek column rahega
#to bhi data milega barobar apne ko isliye extra column ko drop kar dete hai 
dummy_df1 = pd.get_dummies(tips_df,drop_first = True)
print(dummy_df1)

oh_enc = OneHotEncoder(sparse_output=False,drop='First ')
oh_enc_arr = oh_enc.fit_transform(tips_df[['sex','smoker','day','time']])
print(oh_enc_arr)##apne ko ye numpy array me  mila hai to usko convert kar df me 

oh_enc_df = pd.DataFrame(oh_en_arrcolumns=['sex_Male','smoker_Yes','day_Sun','time_Lunch'])
print(oh_enc_df)


