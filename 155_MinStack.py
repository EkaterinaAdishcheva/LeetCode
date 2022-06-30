class MinStack:

    def __init__(self):
        self.stack = []
        self.minElem = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minElem == []:
            self.minElem.append(val)
        else:
            self.minElem.append(min(val, self.minElem[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minElem.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minElem[-1]
        
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()