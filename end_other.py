def end_other(a, b):
	if len(a) > len(b):
		target_s=a.lower()
		source_s=b.lower()
	else:
		target_s=b.lower()
		source_s=a.lower()
	if target_s[-len(source_s):] == source_s:
		return(True)
	return(False)
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

def end_other_f(a,b):
	if len(a) > len(b):
		target_s=a.lower()
		source_s=b.lower()
	else:
		target_s=b.lower()
		source_s=a.lower()
	if target_s.endswith(source_s):
		return(True)
	else:
		return(False)

print(end_other_f('Hiabc', 'abc'))
print(end_other_f('AbC', 'HiaBc'))
print(end_other_f('ab', 'abXabc'))
