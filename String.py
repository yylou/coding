"""
Author  : Yuan-Yao Lou (Mike)
Title   : PhD student in ECE at Purdue University
Email   : yylou@purdue.edu
Website : https://yylou.github.io/
Date    : Feb 05, 2023

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
