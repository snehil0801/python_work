#Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
	new_str=""
	for i in str:
		new_str+=(2*i)
	return(new_str)
print(double_char('The') )
print(double_char('AAbb'))
print(double_char('Hi-There'))
