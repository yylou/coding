"""
Author  : Yuan-Yao Lou (Mike)
Title   : PhD student in ECE at Purdue University
Email   : yylou@purdue.edu
Website : https://yylou.github.io/
Date    : Feb 05, 2023

Project :
    [Coding practice] Tester
"""

from Array                      import Array

class Test:

    @classmethod
    def search(self, id: str):
        if id == "0088": return self._0088_merge_sorted_array()
        if id == "1470": return self._1470_shuffle_array()

    @classmethod
    def run(self, *values, **options):
        if values[0] == "0088": 
            Array._0088_merge_sorted_array(**options)
            print(options["nums1"])

        if values[0] == "1470":
            print(Array._1470_shuffle_array(**options))

    @classmethod
    def _0088_merge_sorted_array(self) -> None:
        #   | Case 1
        nums1 = [1,2,3,0,0,0]
        Array._0088_merge_sorted_array(nums1 = nums1, m = 3, nums2 = [2,5,6], n = 3)
        assert nums1 == [1,2,2,3,5,6]

        input = "nums1 = nums1, m = 3, nums2 = [2,5,6], n = 3"
        answer = "[1,2,2,3,5,6]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        nums1 = [1]
        Array._0088_merge_sorted_array(nums1 = nums1, m = 1, nums2 = [], n = 0)
        assert nums1 == [1]

        input = "nums1 = [1], m = 1, nums2 = [], n = 0"
        answer = "[1]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        nums1 = [0]
        Array._0088_merge_sorted_array(nums1 = nums1, m = 0, nums2 = [1], n = 1)
        assert nums1 == [1]

        input = "nums1 = [0], m = 0, nums2 = [1], n = 1"
        answer = "[1]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _1470_shuffle_array(self) -> None:
        #   | Case 1
        assert Array._1470_shuffle_array(nums = [2,5,1,3,4,7], n = 3) == [2,3,5,4,1,7]

        input = "nums = [2,5,1,3,4,7], n = 3"
        answer = "[2,3,5,4,1,7]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        assert Array._1470_shuffle_array(nums = [1,2,3,4,4,3,2,1], n = 4) == [1,4,2,3,3,2,4,1]

        input = "nums = [1,2,3,4,4,3,2,1], n = 4"
        answer = "[1,4,2,3,3,2,4,1]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        assert Array._1470_shuffle_array(nums = [1,1,2,2], n = 2) == [1,2,1,2]

        input = "nums = [1,1,2,2], n = 2"
        answer = "[1,2,1,2]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")