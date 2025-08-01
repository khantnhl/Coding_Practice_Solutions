"""
uses two stacks
one to store and one to keep track of minimum value
time : O(1)
space: O(n)
"""
class MinStack:

    # stack [1,2,0]
    # minstack [inf, 1,1,0]

    def __init__(self):
        self.stack = []
        self.minstk = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(val < self.minstk[-1]):
            self.minstk.append(val)
        else:
            self.minstk.append(self.minstk[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minstk.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstk[-1]