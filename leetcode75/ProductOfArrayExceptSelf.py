def productExcepSelf(nums):
	l = len(nums)
	prefix = 1
	postfix = 1
	result = [1] * l
    
	for i in range(l):
	    result[i] = prefix
	    print(result)
	    prefix *= nums[i]
	    print(prefix)
	print("------")
	for i in range(l-1, -1, -1):
	    result[i] *= postfix
	    print(result)
	    postfix *= nums[i]
	    print(postfix)

	return result


output=productExcepSelf([1,2,3,4])
print(output)