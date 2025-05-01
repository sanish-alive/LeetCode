def kidsWithCandies(candies, extraCandies):
	greatest = max(candies)
	result = []
	for c in range(len(candies)):
		if candies[c]+extraCandies >= greatest:
			result.append(True)
		else:
			result.append(False)
	return result



output = kidsWithCandies([2,3,5,1,3], 3)
print(output)