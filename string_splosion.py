#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
	result=""
	for i in range(len(str)+1):
		result=result+str[:i]
	return(result)
pr=input("Enter a string: ")
print(string_splosion(pr))
