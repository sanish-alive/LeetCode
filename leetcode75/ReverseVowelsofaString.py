def reverseVowels(s):
	vowels = "aeiouAEIOU"
	s = list(s)
	svowels = []
	for i in range(len(s)):
		if s[i] in vowels:
			svowels.append(s[i])
	sl = len(svowels)
	for i in range(len(s)):
		if s[i] in vowels:
			s[i]=svowels[sl-1]
			sl-=1
	return "".join(s)

output = reverseVowels("IceCreAm")
print(output)