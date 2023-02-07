"""
Author  : Yuan-Yao Lou (Mike)
Title   : PhD student in ECE at Purdue University
Email   : yylou@purdue.edu
Website : https://yylou.github.io/
Date    : Feb 05, 2023

Project :
    [Coding practice] Array
"""

class Array:

    @classmethod
    def search(self, id: str):
        if id == "0027": return self._0027_remove_element
        if id == "0088": return self._0088_merge_sorted_array
        if id == "0217": return self._0217_contains_duplicate
        if id == "0219": return self._0219_contains_duplicate_II
        if id == "0242": return self._0242_valid_anagram
        if id == "0940": return self._0940_fruit_into_baskets
        if id == "1470": return self._1470_shuffle_array

    @classmethod
    def _0027_remove_element(self, nums: list[int], val: int) -> int:
        """
        |  Easy  |  Two Pointer  |
        https://leetcode.com/problems/remove-element/description/
        """

        # Time:  O(n)
        # Space: O(1)

        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return l

    @classmethod
    def _0088_merge_sorted_array(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        |  Easy  |  Two Pointer  |
        https://leetcode.com/problems/merge-sorted-array/
        """

        # Time:  O(m+n)
        # Space: O(1)
        
        p1, p2 = m-1, n-1
        place = m+n-1

        while p1>=0 or p2>=0:
            val1 = nums1[p1] if p1 >= 0 else float("-inf")
            val2 = nums2[p2] if p2 >= 0 else float("-inf")

            if val1 > val2:     # nums1[p1] = val1
                nums1[place] = val1
                p1 -= 1
            else:               # nums2[p2] = val2
                nums1[place] = val2
                p2 -= 1

            place -= 1

    @classmethod
    def _0217_contains_duplicate(self, nums: list[int]) -> bool:
        """
        |  Easy  |  Hash  |
        |https://leetcode.com/problems/contains-duplicate
        """

        # Time:  O(n)
        # Space: O(n)

        table = set()
        for num in nums:
            if num in table: break
            table.add(num)
        else: return False
        return True

    @classmethod
    def _0219_contains_duplicate_II(self, nums: list[int], k: int) -> bool:
        """
        |  Easy  |  Sliding Window + Hash  |
        https://leetcode.com/problems/contains-duplicate-ii
        """

        def solution_1(nums: list[int], k: int) -> bool:
            
            # Time:  O(n)
            # Space: O(n)

            table = set()
            l, r = 0, 0

            while r < len(nums):
                if r - l > k:
                    table.remove(nums[l])
                    l += 1
                if nums[r] in table: return True
                table.add(nums[r])
                r += 1
            return False
        
        def solution_2(nums: list[int], k: int) -> bool:

            # Time:  O(n)
            # Space: O(n)

            table = {}

            for r in range(len(nums)):
                if nums[r] not in table: 
                    table[nums[r]] = r
                else:
                    if r - table[nums[r]] <= k: return True
                    table[nums[r]] = r
            return False

        ans1, ans2 = solution_1(nums=nums, k=k), solution_2(nums=nums, k=k)
        assert ans1 == ans2, "(0219) Two solutions have different answers"
        return ans1

    @classmethod
    def _0242_valid_anagram(self, s: str, t: str) -> bool:
        """
        |  Easy  |  Hash  |  https://leetcode.com/problems/valid-anagram
        """

        # Time:  O(max(n, m))
        # Space: O(n)

        from collections import Counter

        counter = Counter(s)
        for char in t:
            if char not in counter: return False    # extra
            if counter[char] <= 0 : return False    # not enough
            counter[char] -= 1
        
        if any(counter.values()): return False      # remain
        return True

    @classmethod
    def _0940_fruit_into_baskets(self, fruits: list[int]) -> int:
        """
        |  Medium  |  Sliding Window + Hash  |
        https://leetcode.com/problems/fruit-into-baskets/
        """

        # Time:  O(n)
        # Space: O(n)

        table = {}
        maximum = float("-inf")
        l = 0

        for r in range(len(fruits)):
            table[fruits[r]] = table.get(fruits[r], 0) + 1
            while len(table) > 2:
                maximum = max(maximum, sum(table.values())-1)
                table[fruits[l]] -= 1
                if table[fruits[l]] < 1: del table[fruits[l]]
                l += 1

        maximum = max(maximum, sum(table.values()))
        return maximum

    @classmethod
    def _1470_shuffle_array(self, nums: list[int], n: int) -> list:
        """
        |  Easy  |  Bit Operation  |
        https://leetcode.com/problems/shuffle-the-array/
        """

        # Time:  O(n)
        # Space: O(1)

        for i in range(n): nums[i] |= (nums[i+n] << 10)
        MASK = int(pow(2, 10)) - 1

        #   (in-place by reverse order)
        for i in range(n-1, -1, -1):
            idx = 2 * i
            val = nums[i]
            nums[idx], nums[idx+1] = val & MASK, val >> 10

        return nums
