def reverseList(head):
    left = 0
    right = len(head)-1
    while left<right:
        temp = head[left]
        head[left] = head[right]
        head[right] = temp
        right-=1
        left+=1
    return head

print(reverseList([1,2,3,4,5,6]))
