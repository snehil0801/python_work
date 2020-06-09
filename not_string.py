'''
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string("candy") => not candy
not_string("x") => not x 
not_string("not bad") => not bad


'''
def not_string(str):
	print("not found in string at", str.find('not',0))
	return(str.find('not',0))
s = input("Enter a string: ")
f=not_string(s)
print(f)
if(f):
	print(True)
else:
	print(False)
