# Not Solved.
def increasingTriplet(nums):
	for i in range(1, len(nums)-1):
		if nums[i-1] < nums[i] < nums[i+1]:
			return True
	return False

print(increasingTriplet([5,4,3,2,1]))