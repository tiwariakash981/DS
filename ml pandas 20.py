import pandas as pd

emp_df = pd.DataFrame()
print(emp_df)

list1 = ['a','b','c']
print(list1)

df = pd.DataFrame(list1)
print("printing list using DataFrame()\n",df)

ls_of_ls = [[1,2,3],[3,4,5],[5,6,7]]
print("list of list:",ls_of_ls)
print("list_of_list using DataFrame",pd.DataFrame(ls_of_ls))

dict1 = {'id1':[11,12,13,14]}
print("printing values of a dictionary",dict1)

dict2 = {'id1':[11,12,13,14],'sn':[22,33,44,55]}
print("printing values of dictionary using dataframe\n",pd.DataFrame(dict2))

list_of_dictionary = [{'a':(1,2,3,4),'b':(4,5)},{'a':(6,7),'b':(5,6,7,77)}]
print("list_of_dictionary :",list_of_dictionary)
print("converting list_of_dictionary into DataFrame()\n",pd.DataFrame(list_of_dictionary))

dictionary_of_series = {'id':pd.Series([1,2,3]),'sn':pd.Series([9,5,6])}
print("printing dictionary_of_series",pd.DataFrame(dictionary_of_series))
















