def validParentheses(s):
	stack = []
	closeToOpen = { ")" : "(", "{" : "}", "]" : "["}

	for p in s:
		if p in closeToOpen:
			if stack and stack[-1] == closeToOpen[p]:
				stack.pop
			else:
				return False
		else:
			stack.append(p)
	return True if not stack else False
print(validParentheses("()[]{}"))