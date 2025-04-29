def mergeAlternately(word1, word2):
	result=""
	length1 = len(word1)
	length2 = len(word2)

	if length1==length2:
		for i in range(0, length1):
			result += word1[i]+word2[i]
	elif length1 > length2:
		for i in range(0, length2):
			result += word1[i]+word2[i]
		result+=word1[i+1:]
	else:
		for i in range(0, length1):
			result += word1[i]+word2[i]
		result+=word2[i+1:]
	return result


def betterMergeAlternately(word1, word2):
	result=""
	maxlen = max(len(word1), len(word2))
	for i in range(maxlen):
		if i<len(word1):
			result+=word1[i]
		if i<len(word2):
			result+=word2[i]
	return result

result = betterMergeAlternately("abcjhkjb", "pqrmn")
print(result)