# https://leetcode.com/problems/implement-stack-using-queues/
# Easy
# Note: Just implement a stack?

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return None
        
        pop = int(self.stack[-1])
        self.stack = self.stack[:-1]
        return pop

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return []
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.stack
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()