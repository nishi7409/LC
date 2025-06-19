class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        return self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return 0
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return 0
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()