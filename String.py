"""
Author  : Yuan-Yao Lou (Mike)
Title   : PhD student in ECE at Purdue University
Email   : yylou@purdue.edu
Website : https://yylou.github.io/
Date    : Feb 14, 2023

Project :
    [Coding practice] String
"""

class String:

    @classmethod
    def search(self, id: str):
        for function, object in self.__dict__.items():
            if function[1:5] == id: return object
        return None

    @classmethod
    def _0020_valid_parentheses(self, s: str) -> bool:
        """  Easy  |  Stack  """
        # Time:  O(n)
        # Space: O(n)

        mapping = {"]": "[", ")": "(", "}": "{"}
        stack = []
        for char in s:
            if char in mapping:
                if not stack: return False  # un-opened
                if stack.pop() != mapping[char]: return False   # un-matched
            else:
                stack.append(char)
        
        if stack: return False      # un-closed
        return True

    @classmethod
    def _0022_generate_parentheses(self, n: int) -> list[str]:
        def solution_1(n):
            """  Medium  |  BFS  """
            # Time:  O(n * m * length)
            # Space: O(m)

            ans = ["()"]
            for i in range(1, n):
                tmp = set()
                for string in ans:
                    for idx in range(len(string)):
                        tmp.add(f"{string[:idx]}{'()'}{string[idx:]}")
                ans = tmp

            return ans

        def solution_2(n):
            """  Medium  |  DFS, Backtracking  """
            # Time:  O()
            # Space: O()
            
            ans = []
            def dfs(string: str, left: int, right: int):
                if n == left == right:
                    ans.append(string)
                
                else:
                    if left < n: dfs(string + '(', left + 1, right)
                    if right < left: dfs(string + ')', left, right + 1)

            dfs("", 0, 0)
            return ans

        return solution_1(n=n)
        return solution_2(n=n)

    @classmethod
    def _0125_valid_palindrome(self, s: str) -> bool:
        """  Easy  |  Two Pointer  """
        # Time:  O(n)
        # Space: O(1)

        l, r = 0, len(s)-1
        while l < r:
            #   (skip non-qualified char)
            while l < len(s) and s[l].isalnum() == False: l += 1
            while r >= 0     and s[r].isalnum() == False: r -= 1

            if l >= len(s) or r < 0 or l >= r: return True  # (empty)
            if s[l].lower() != s[r].lower(): return False   # (non-palidrome)

            l += 1
            r -= 1
        
        return True
