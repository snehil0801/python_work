numbers = [45, 22, 14, 65, 97, 72]
for i,num in enumerate(numbers):
	if num%3 == 0 and num%5 == 0:
		numbers[i]='fizbuzz'
	elif num%3 == 0:
		numbers[i]='fizz'
	elif num%5 == 0:
		numbers[i]='buzz'
print(numbers)