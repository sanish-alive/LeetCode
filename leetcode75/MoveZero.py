def moveZeroes(nums):
	j=0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[j], nums[i] = nums[i], nums[j]
			j+=1
		print(nums)
	return nums


print(moveZeroes([0,1,0,3,12]))