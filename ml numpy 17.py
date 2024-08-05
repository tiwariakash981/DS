import numpy as np

char1 = "Akash Manager "
char2 = "Tiwari"

print("adding char1 and char2",np.char.add(char1,char2))

print("making lowercase to char1",np.char.lower(char1))
print("making uppercase to char1",np.char.upper(char1))

print("we can centralize our character ",np.char.center(char1,30,fillchar="*"))

print("splitting the character ",np.char.split(char1))

print(r"split any lines if there is any \n ",np.char.splitlines("hello\nbro"))

str1 = "dmy"
str2 = "dmy"
print("adding s value to each character",np.char.join([":","/"],[str1,str2]))
print("replacing vlaues ",np.char.replace(str1,"dmy","ak"))
print("counting values of string",np.char.count(str1,"dmy"))
print("finding index value using find() function",np.char.find(str1,"dm"))
