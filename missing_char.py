def missing_char(str,n):
	return(str[:n]+str[n+1:])
str=input("enter a string: ")
ind=int(input("enter a index: "))
print(missing_char(str,ind))