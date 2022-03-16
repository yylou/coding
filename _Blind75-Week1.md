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

## 0121. Best Time to Buy and Sell Stock ```Easy```     <a name="p3"></a>
---
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

## 0242. Valid Anagram ```Easy```                       <a name="p4"></a>
LeetCode link: [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)
```python
```

## 0020. Valid Parentheses ```Easy```                   <a name="p5"></a>
LeetCode link: [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)
```python
```

## 0053. Maximum Subarray ```Easy```                    <a name="p6"></a>
LeetCode link: [https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)
```python
```

## 0238. Product of Array Except Self ```Medium```      <a name="p7"></a>
LeetCode link: [https://leetcode.com/problems/product-of-array-except-self/](https://leetcode.com/problems/product-of-array-except-self/)
```python
```

## 0015. 3Sum ```Medium```                              <a name="p8"></a>
LeetCode link: [https://leetcode.com/problems/3sum/](https://leetcode.com/problems/3sum/)
```python
```

## 0056. Merge Intervals ```Medium```                   <a name="p9"></a>
LeetCode link: [https://leetcode.com/problems/merge-intervals/](https://leetcode.com/problems/merge-intervals/)
```python
```

## 0049. Group Anagrams ```Medium```                    <a name="p10"></a>
LeetCode link: [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)
```python
```

## 0152. Maximum Product Subarray ```Medium```          <a name="p11"></a>
LeetCode link: [https://leetcode.com/problems/maximum-product-subarray/](https://leetcode.com/problems/maximum-product-subarray/)
```python
```

## 0033. Search in Rotated Sorted Array ```Medium```    <a name="p12"></a>
LeetCode link: [https://leetcode.com/problems/search-in-rotated-sorted-array/](https://leetcode.com/problems/search-in-rotated-sorted-array/)
```python
```