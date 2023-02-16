"""
Author  : Yuan-Yao Lou (Mike)
Title   : PhD student in ECE at Purdue University
Email   : yylou@purdue.edu
Website : https://yylou.github.io/
Date    : Feb 16, 2023

Project :
    [Coding practice] Stack
"""

class Stack:

    @classmethod
    def search(self, id: str):
        for function, object in self.__dict__.items():
            if function[1:5] == id: return object
        return None

    @classmethod
    def _0155_min_stack(self) -> list:
        """  Medium  |  Stack  """
        # Time:  O(1)

        class MinStack:
            def __init__(self):
                self.stack = []

            def push(self, val: int) -> None:
                if len(self.stack) == 0:
                    self.stack.append((val, val))
                else:
                    MIN = self.getMin()
                    self.stack.append((val, min(val, MIN)))

            def pop(self) -> None:
                # MinStack can only pop top element
                # while MinHeap pops MIN element
                val, curMIN = self.stack.pop()

            def top(self) -> int:
                if len(self.stack) == 0: return None
                return self.stack[-1][0]

            def getMin(self) -> int:
                if len(self.stack) == 0: return None
                return self.stack[-1][1]
        
        ans = []
        minStack = MinStack()
        ans.append(minStack.push(-2))
        ans.append(minStack.push(0))
        ans.append(minStack.push(-3))
        ans.append(minStack.getMin())
        ans.append(minStack.pop())
        ans.append(minStack.top())
        ans.append(minStack.getMin())
        return ans