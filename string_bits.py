#Given a string, return a new string made of every other char starting with the first, so
def string_bits(str):
	return(str[::2])
pr=input("Enter a string: ")
print(string_bits(pr))