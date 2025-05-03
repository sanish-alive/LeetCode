def increasingTriplet(nums):
	triplet=0
	smallest=nums[0]
	for i in range(1, len(nums)):
		print(smallest)
		if smallest<nums[i]:			
			triplet+=1
			if triplet==3:
				return True
		if nums[i]<nums[i-1]:
			smallest=nums[i]
		print(triplet)
	return False

print(increasingTriplet([0,4,2,10,-1,-3]))