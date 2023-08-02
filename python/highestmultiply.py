def highest(arrs):
	highestmultiply = 0
	for i in range(len(arrs)):
		for j in range(i+1, len(arrs)):
			for k in range(j+1, len(arrs)):
				multi = arrs[i] * arrs[j] * arrs[k]
				if (multi > highestmultiply):
					highestmultiply = multi
	return highestmultiply


arrs = [6,2,3,4,5]
print(highest(arrs))
