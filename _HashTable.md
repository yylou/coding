# Python Coding

* ### [Menu](./README.md)
* ### Data Structures - Hash Table
    * [<ins>Source Code<ins>](./_HashTable.py)
    * [Anagram](#p1)
* ### LeetCode Problems
    * [0049. Group Anagrams (Medium)](https://leetcode.com/problems/group-anagrams/)
    * [0138. Copy List with Random Pointer (Medium)](https://leetcode.com/problems/copy-list-with-random-pointer/)
    * [0242. Valid Anagram (Easy)](https://leetcode.com/problems/valid-anagram/)
    * [0409. Longest Palindrome (Easy)](https://leetcode.com/problems/longest-palindrome/)
    * [0438. Find All Anagrams in a String (Medium)](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

<br />

## Anagram                                  <a name="p1"></a>
An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

```python
"""
0049. Group Anagrams (Medium)
https://leetcode.com/problems/group-anagrams/
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # (base case)
        if not strs: return [[""]]
        if len(strs) == 1: return [strs]
        
        table = {}
        for element in strs:
            # (1) Using occurency as key
            # key = self.count(element)
            
            # (2) Using sorted string as key
            key = ''.join(sorted(element))
            
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
https://leetcode.com/problems/valid-anagram/
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # (base case) Non-equal length / length == 1
        if len(s) != len(t): return False
        if len(s) == 1 and len(t) == 1: return s[0] == t[0]
        
        table = Counter(s)
        
        for char in t:
            # Additional char
            if char not in table: return False
            
            table[char] -= 1
            
            # Not enough chars
            if table[char] < 0: return False
        
        # Remain chars
        for val in table.values():
            if val != 0: return False
        
        return True
```

```python
"""
0409. Longest Palindrome (Easy)
https://leetcode.com/problems/longest-palindrome/
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # (base case)
        if len(s) == 1: return 1
        
        table = Counter(s)
        
        length = 0
        for k, v in table.items():
            # Even occurence: take all
            # Odd  occurence: take all and only left 1
            result, remain = divmod(v, 2)
            length += v - remain
            
            # Current length is even and char still remains
            if length % 2 == 0 and v % 2 == 1: length += 1
            
        return length
```

```python
"""
0438. Find All Anagrams in a String (Medium)
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # (base case)
        if len(p) > len(s): return []
        
        ans = []
        table, n = Counter(p), len(p)
        tmpTable = Counter(s[:n])
        if table == tmpTable: ans.append(0)
        
        # Sliding Window
        for i in range(n, len(s)):
            # 1. Remove previous char
            tmpTable[s[i-n]] -= 1
            if tmpTable[s[i-n]] < 0: del tmpTable[s[i-n]]
                
            # 2. Add new char
            tmpTable[s[i]] = tmpTable.get(s[i], 0) + 1
            
            # 3. Check
            if table == tmpTable: ans.append(i + 1 - n)
                
        return ans
```