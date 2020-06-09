#Return list with square of numbers
def squ(num):
	return num*num
def is_odd(num):
	return bool(num%2)

lis1=[4, 2, 1, 6, 9, 7]
result_list=[squ(x) for x in lis1]
print(result_list)
filtered_list=[ x for x in lis1 if is_odd(x)]	
print(filtered_list)

