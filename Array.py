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
        if id == "0088": return self._0088_merge_sorted_array
        if id == "1470": return self._1470_shuffle_array

    @classmethod
    def _0088_merge_sorted_array(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Easy  |  Two Pointer  |  https://leetcode.com/problems/merge-sorted-array/
        """
        
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
    def _1470_shuffle_array(self, nums: list, n: int) -> list:
        """
        Easy  |  Bit Operation  |  https://leetcode.com/problems/shuffle-the-array/
        """

        for i in range(n): nums[i] |= (nums[i+n] << 10)
        MASK = int(pow(2, 10)) - 1

        #   (in-place by reverse order)
        for i in range(n-1, -1, -1):
            idx = 2 * i
            val = nums[i]
            nums[idx], nums[idx+1] = val & MASK, val >> 10

        return nums
            