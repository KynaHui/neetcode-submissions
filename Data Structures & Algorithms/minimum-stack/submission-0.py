# time: O(1)
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # min value at that index

    def push(self, value: int) -> None:
        self.stack.append(value)
        # if minStack empty, min(value, value)
        # value = min(value, self.minStack[-1] if self.minStack else value)
        if self.minStack: 
            value = min(value, self.minStack[-1])
        self.minStack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # no edge case, pop() is called on non-empty stack
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()