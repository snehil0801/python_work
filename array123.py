#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums, seq):
	for i in range(len(nums)+1):
		if nums[i:i+len(seq)] == seq:
			print(i)
			return(True)

print(array123([1, 9, 9,9],[9,9]))