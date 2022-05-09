# Python Coding

* ### [Menu](./README.md)
* ### Data Structures - Hash Table
    * [Anagram / Palindrome](#p1)
* ### LeetCode Problems
    * [0001. Two Sum ```Easy```](https://leetcode.com/problems/two-sum/)
    * [0015. 3Sum ```Medium```](https://leetcode.com/problems/3sum/)
    * [0049. Group Anagrams ```Medium```](https://leetcode.com/problems/group-anagrams/)
    * [0138. Copy List with Random Pointer ```Medium```](https://leetcode.com/problems/copy-list-with-random-pointer/)
    * [0217. Contains Duplicate ```Easy```](https://leetcode.com/problems/contains-duplicate/)
    * [0242. Valid Anagram ```Easy```](https://leetcode.com/problems/valid-anagram/)
    * [0409. Longest Palindrome ```Easy```](https://leetcode.com/problems/longest-palindrome/)
    * [0438. Find All Anagrams in a String ```Medium```](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

<br />

## Anagram / Palindrome                     <a name="p1"></a>
* An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
* A phrase is a **Palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

```python
"""
0049. Group Anagrams (Medium)
https://leetcode.com/problems/group-anagrams
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        # ==================================================
        #  [Array] Hash Table, Sort                        =
        # ==================================================
        # time  : O(n * mlogm)
        # space : O(1)
        """
        
        # (base case)
        if not strs: return [['']]
        if len(strs) == 1: return [strs]
        
        table = {}
        for element in strs:
            # (1) Using occurency as key
            # key = self.count(element)
            
            # (2) Using sorted string as key
            key = tuple(sorted(element))
            
            table[key] = table.get(key, []) + [element]
            
        return table.values()
        
    def count(self, s: str):
        """
        Count the occurence based on 26 lowercase Engligh letters
        """
        counter = [0 for _ in range(26)]
        for char in s: counter[ord(char) - ord('a')] += 1
        return tuple(counter)
```

```python
"""
0242. Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        # ==================================================
        #  [String] Hash Table                             =
        # ==================================================
        # time  : O(m + n)
        # space : O(n)
        """
        
        # (base case) Non-equal length / length == 1
        if len(s) != len(t): return False
        if len(s) == 1 and len(t) == 1: return s[0] == t[0]
        
        table = Counter(s)
        
        for char in t:
            # (1)   Additional char
            if char not in table: return False
            
            table[char] -= 1
            
            # (2)   Not enough char
            if table[char] < 0: return False
        
        # (3)   Remaining char
        if any(counter.values()): return False
        
        return True
```

```python
"""
0409. Longest Palindrome (Easy)
https://leetcode.com/problems/longest-palindrome
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        """
        # ==================================================
        #  [String] Hash Table (Counter), Math             =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """
        
        # (base case)
        if len(s) == 1: return 1
        
        table = Counter(s)
        
        length = 0
        for k, v in table.items():
            # (1)   Take even number of occurence
            result, remain = divmod(v, 2)
            length += v - remain
            
            # (2)   Current length is even and char still remains
            if length % 2 == 0 and remain == 1: length += 1
            
        return length
```

```python
"""
0438. Find All Anagrams in a String (Medium)
https://leetcode.com/problems/find-all-anagrams-in-a-string
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        """
        # ==================================================
        #  [String] Sliding Window                         =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        """
        
        # (base case)
        if len(p) > len(s): return []
        
        n = len(p)
        current = sum(hash(char) for char in s[:n])
        target  = sum(hash(char) for char in p)
        
        ans = []
        if current == target: ans.append(0)
        
        for i, v in enumerate(s[n:]):
            current += hash(v) - hash(s[i])
            if current == target: ans.append(i + 1)
            
        return ans
```