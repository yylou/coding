# Python Coding

* ### [Menu](./README.md)                   <a name="p0"></a>
* ### Blind 75 Leetcode Problems - Week 1
    * [0001. Two Sum ```Easy```](#p1)
    * [0217. Contains Duplicate ```Easy```](#p2)
    * [0121. Best Time to Buy and Sell Stock ```Easy```](#p3)
    * [0242. Valid Anagram ```Easy```](#p4)
    * [0020. Valid Parentheses ```Easy```](#p5)
    * [0053. Maximum Subarray ```Easy```](#p6)
    * [0238. Product of Array Except Self ```Medium```](#p7)
    * [0015. 3Sum ```Medium```](#p8)
    * [0056. Merge Intervals ```Medium```](#p9)
    * [0049. Group Anagrams ```Medium```](#p10)
    * [0152. Maximum Product Subarray ```Medium```](#p11)
    * [0033. Search in Rotated Sorted Array ```Medium```](#p12)

<br />

## 0001. Two Sum ```Easy```                             <a name="p1"></a>
LeetCode link: [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        # ==================================================
        #  [Array] Hash Table                              =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        """
        
        # (base case)
        if len(nums) == 2: return [0, 1]
        
        table = {}
        for i in range(len(nums)):
            if target - nums[i] not in table: table[nums[i]] = i
            else: return [table[target - nums[i]], i]
```

<br />

## 0217. Contains Duplicate ```Easy```                  <a name="p2"></a>
LeetCode link: [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        """
        # ==================================================
        #  [Array] Hash Table                              =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        """
        
        # (base case)
        if len(nums) == 1: return False
        
        table = set()
        for num in nums:
            if num in table: return True
            table.add(num)
            
        return False
```

<br />

## 0121. Best Time to Buy and Sell Stock ```Easy```     <a name="p3"></a>
LeetCode link: [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        # ==================================================
        #  [Array] DP                                      =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """
        
        # (base case)
        if len(prices) == 1: return 0
        
        # (1) Hold stock, or no stock on hold
        hold, noHold = float('-inf'), 0
        
        for price in prices:
            preHold, preNoHold = hold, noHold
            
            hold   = max(preHold,   0 - price)
            noHold = max(preNoHold, preHold + price)
            
        return noHold
```

<br />

## 0242. Valid Anagram ```Easy```                       <a name="p4"></a>
LeetCode link: [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)
```python
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
            # (1) Additional char
            if char not in table: return False
            
            table[char] -= 1
            
            # (2) Not enough chars
            if table[char] < 0: return False
        
        # (3) Remain chars
        for val in table.values():
            if val != 0: return False
        
        return True
```

<br />

## 0020. Valid Parentheses ```Easy```                   <a name="p5"></a>
LeetCode link: [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)
```python
class Solution:
    def isValid(self, s: str) -> bool:
        
        """
        # ==================================================
        #  [String] Stack                                  =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        """
        
        # (base case)
        if len(s) == 1: return False
        
        table = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            if char not in table: stack.append(char)
            else:
                if not stack: return False
                if stack.pop() != table[char]: return False
        
        # Check for any unclosed parentheses
        if stack: return False
        
        return True
```

<br />

## 0053. Maximum Subarray ```Easy```                    <a name="p6"></a>
LeetCode link: [https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        # ==================================================
        #  [Array] DP (curSum, maxSum)                     =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """
        
        # (base case)
        if len(nums) == 1: return nums[0]
        
        curSum = maxSum = float('-inf')
        
        for num in nums:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
            
        return maxSum
```

<br />

## 0238. Product of Array Except Self ```Medium```      <a name="p7"></a>
LeetCode link: [https://leetcode.com/problems/product-of-array-except-self/](https://leetcode.com/problems/product-of-array-except-self/)
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        # ==================================================
        #  [Array] Two Pass                                =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        """
        
        # (base case)
        if len(nums) == 2: return [nums[1], nums[0]]
        
        ans = [None for _ in range(len(nums))]
        
        # [1, 1*a0, 1*a0*a1, 1*a0*a1*a2]
        cur = 1
        for i in range(len(nums)):
            ans[i] = cur
            cur = nums[i] * cur
        
        # [1*a1*a2*a3, 1*a2*a3, 1*a3, 1]
        cur = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * cur
            cur = nums[i] * cur
            
        return ans
```

<br />

## 0015. 3Sum ```Medium```                              <a name="p8"></a>
LeetCode link: [https://leetcode.com/problems/3sum/](https://leetcode.com/problems/3sum/)
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.bruteForce(nums)
        return self.space(nums)
        return self.twoPointer(nums)

    def bruteForce(self, nums: List[int]) -> List[List[int]]:
        
        """
        # ==================================================
        #  [Array] Brute Force                             =
        # ==================================================
        # time  : O(n^2)
        # space : O(1)
        """
        
        # (base case)
        if not nums or len(nums) < 3: return []
        
        ans = set()
        for i in range(len(nums)):
            table = {}
            target = 0 - nums[i]
            
            for j in range(len(nums)):
                if i == j: continue
                remain = target - nums[j]
                
                if remain in table: ans.add(tuple(sorted([nums[i], remain, nums[j]])))
                table[nums[j]] = j
        
        return ans
        
    def space(self, nums: List[int]) -> List[List[int]]:
        
        """
        # ==================================================
        #  [Array] Two Pass, Hash Table                    =
        # ==================================================
        # time  : O(n^2)
        # space : O(n)
        """
        
        # (base case)
        if not nums or len(nums) < 3: return []
        
        ans = set()
        zero, neg, pos = [], [], []
        for num in nums:
            if num == 0: zero.append(num)
            if num  > 0: pos.append(num)
            if num  < 0: neg.append(num)
        
        # (0, 0, 0)
        if len(zero) > 2: ans.add((0, 0, 0))
            
        _neg, _pos = set(neg), set(pos)
        
        # (-n, 0, n)
        if zero:
            for element in _pos:
                if element * -1 in _neg: ans.add((element*-1, 0, element))
        
        # (-n, -n, n)
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                remain = -1 * (neg[i] + neg[j])
                if remain in _pos: ans.add(tuple(sorted([remain, neg[i], neg[j]])))
        
        # (-n, n, n)
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                remain = -1 * (pos[i] + pos[j])
                if remain in _neg: ans.add(tuple(sorted([remain, pos[i], pos[j]])))
        
        return ans
    
    def twoPointer(self, nums: List[int]) -> List[List[int]]:
        
        """
        # ==================================================
        #  [Array] Sort, Two Pointer                       =
        # ==================================================
        # time  : O(nlogn + n^2)
        # space : O(1)
        """
        
        # (base case)
        if not nums or len(nums) < 3: return []
        
        ans = set()
        nums.sort()
        
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if   total > 0: r -= 1
                elif total < 0: l += 1
                else: 
                    ans.add((nums[i], nums[l], nums[r]))
                    
                    # (optional) Skip duplicates to reduce runtime
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    
                    l, r = l+1, r-1
                    
        return ans
```

<br />

## 0056. Merge Intervals ```Medium```                   <a name="p9"></a>
LeetCode link: [https://leetcode.com/problems/merge-intervals/](https://leetcode.com/problems/merge-intervals/)
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        """
        # ==================================================
        #  [Array] Sort (using start index)                =
        # ==================================================
        # time  : O(nlogn + n)
        # space : O(1)
        """
        
        # (base case)
        if len(intervals) == 1: return intervals
        
        # Make start index be ascending
        intervals.sort(key=lambda x: x[0])
        ans = []
        
        for element in intervals:
            start, end = element
            
            # (1) No overlap by checking end index: append
            if not ans or start > ans[-1][-1]: ans.append(element)
            
            # (2) Overlap: update
            else: ans[-1][-1] = max(ans[-1][-1], end)
                
        return ans
```

<br />

## 0049. Group Anagrams ```Medium```                    <a name="p10"></a>
LeetCode link: [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)
```python
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

<br />

## 0152. Maximum Product Subarray ```Medium```          <a name="p11"></a>
LeetCode link: [https://leetcode.com/problems/maximum-product-subarray/](https://leetcode.com/problems/maximum-product-subarray/)
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        """
        # ==================================================
        #  [Array] DP (curMax, curMin, maxSum)             =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """
        
        # (base case)
        if len(nums) == 1: return nums[0]
        
        maxSum = curMax = curMin = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            candidate = (num, num*curMax, num*curMin)

            curMax, curMin = max(candidate), min(candidate)
            maxSum = max(maxSum, curMax)
            
        return maxSum
```

<br />

## 0033. Search in Rotated Sorted Array ```Medium```    <a name="p12"></a>
LeetCode link: [https://leetcode.com/problems/search-in-rotated-sorted-array/](https://leetcode.com/problems/search-in-rotated-sorted-array/)
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.method1(nums, target)
        return self.method2(nums, target)
    
    def method1(self, nums: List[int], target: int) -> int:
        """
        # ==================================================
        #  [Array] Binary Search                           =
        # ==================================================
        # time  : O(logn)
        # space : O(1)
        """
        
        # (base case)
        if len(nums) == 1: return 0 if target == nums[0] else -1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = (l + r) // 2
            
            if nums[pivot] == target:
                return pivot
            
            if nums[pivot] >= nums[l]:
                if nums[pivot] > target >= nums[l]:
                    r = pivot - 1
                else:
                    l = pivot + 1
                    
            else:
                if nums[r] >= target > nums[pivot]:
                    l = pivot + 1
                else:
                    r = pivot - 1
                    
        return -1
    
    def method2(self, nums: List[int], target: int) -> int:
        """
        # ==================================================
        #  [Array] Binary Search                           =
        # ==================================================
        # time  : O(logn)
        # space : O(1)
        """
        
        # (base case)
        if len(nums) == 1: return 0 if target == nums[0] else -1
        
        minIndex = self.findMin(nums)
        if target == nums[minIndex]: return minIndex
        
        index = -1
        if minIndex == 0:
            index = self.binarySearch(nums, target, 0, len(nums) - 1)
        
        elif nums[minIndex - 1] >= target >= nums[0]:
            index = self.binarySearch(nums, target, 0, minIndex)
        
        elif nums[len(nums) - 1] >= target >= nums[minIndex]:
            index = self.binarySearch(nums, target, minIndex, len(nums) - 1)
        
        return index
    
    def binarySearch(self, nums: List[int], target: int, l: int, r: int) -> int:
        
        """
        # ==================================================
        #  [Array] Binary Search                           =
        #          (Leetcode 704)                          =
        # ==================================================
        # time  : O(logn)
        # space : O(1)
        """
        
        while l <= r:
            pivot = (l + r) // 2
            
            if nums[pivot] == target:
                return pivot
            
            if nums[pivot] > target: r = pivot - 1
            else: l = pivot + 1
                
        return -1
    
    def findMin(self, nums: List[int]) -> int:
        
        """
        # ==================================================
        #  [Array] Binary Search                           =
        #          (Leetcode 153)                          =
        # ==================================================
        # time  : O(logn)
        # space : O(1)
        """
        
        # (base case)
        if len(nums) == 1 or nums[0] < nums[-1]: return 0
        
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = (l + r) // 2
            
            if nums[pivot - 1] > nums[pivot]:
                return pivot
            
            if nums[pivot] > nums[r]: l = pivot + 1
            else: r = pivot - 1
```