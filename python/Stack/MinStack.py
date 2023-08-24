class MinStack(object):

    def __init__(self):
        self.stack = []
        self.stackMin = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.stackMin[-1] if self.stackMin else val)
        self.stackMin.append(val)


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.stackMin.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stackMin[-1]
        
obj = MinStack()
obj.push(21)
obj.push(29)
obj.push(33)
obj.push(5)
obj.push(12)
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)