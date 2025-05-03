def reverseWords(s):
	slist = s.split()
	result=""
	l, r = 0, len(slist)-1
	while l<r:
		slist[l], slist[r] = slist[r], slist[l]
		l+=1
		r-=1
	return " ".join(slist)


output=reverseWords("This is a friend")
print(output)