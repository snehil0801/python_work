#Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
	cat_c=str.count('cat')
	dog_c=str.count('dog')
	if cat_c == dog_c:
		return(True)
	return(False)
def cat_dog_fl(str):
	cat_c=0
	dog_c=0
	for i in range(len(str)-1):
		if str[i:i+3] == 'cat':
			cat_c+=1
		if str[i:i+3] == 'dog':
			dog_c+=1
	if cat_c == dog_c:
		return(True)
	return(False)

print(cat_dog('catdog'))
print(cat_dog_fl('catdog'))
print(cat_dog('catcat'))
print(cat_dog_fl('catcat'))
print(cat_dog('1cat1cadodog'))
print(cat_dog_fl('1cat1cadodog'))


