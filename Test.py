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
    def run(self, *values, **options):
        if values[0] == "0027": Array._0027_remove_element(**options); print(options["nums"])
        if values[0] == "0088": Array._0088_merge_sorted_array(**options); print(options["nums1"])
        if values[0] == "0217": print(Array._0217_contains_duplicate(**options))
        if values[0] == "0219": print(Array._0219_contains_duplicate_II(**options))
        if values[0] == "0242": print(Array._0242_valid_anagram(**options))
        if values[0] == "0940": print(Array._0940_fruit_into_baskets(**options))
        if values[0] == "1470": print(Array._1470_shuffle_array(**options))

    @classmethod
    def search(self, id: str):
        if id == "0027": return self._0027_remove_element()
        if id == "0088": return self._0088_merge_sorted_array()
        if id == "0217": return self._0217_contains_duplicate()
        if id == "0219": return self._0219_contains_duplicate_II()
        if id == "0242": return self._0242_valid_anagram()
        if id == "0940": return self._0940_fruit_into_baskets()
        if id == "1470": return self._1470_shuffle_array()

    @classmethod
    def _0027_remove_element(self) -> None:
        #   | Case 1
        nums, val = [3,2,2,3], 3
        assert Array._0027_remove_element(nums=nums, val=val) == 2
        assert val not in set(nums[:2]), f"Key value not being removed: {nums}"
        input = 'nums = [3,2,2,3], val = 3'
        answer = 2
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}, {nums[:answer]}")

        #   | Case 2
        nums, val = [0,1,2,2,3,0,4,2], 2
        assert Array._0027_remove_element(nums=nums, val=val) == 5
        assert val not in set(nums[:5]), f"Key value not being removed: {nums}"
        input = 'nums = [0,1,2,2,3,0,4,2], val = 2'
        answer = 5
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}, {nums[:answer]}\n")
    
    @classmethod
    def _0088_merge_sorted_array(self) -> None:
        #   | Case 1
        nums1 = [1,2,3,0,0,0]
        Array._0088_merge_sorted_array(nums1 = nums1, m = 3, nums2 = [2,5,6], n = 3)
        assert nums1 == [1,2,2,3,5,6]
        input = "nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3"
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
    def _0217_contains_duplicate(self) -> None:
        #   | Case 1
        assert  Array._0217_contains_duplicate(nums = [1,2,3,1]) == True
        input = "nums = [1,2,3,1]"
        answer = "True"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        assert  Array._0217_contains_duplicate(nums = [1,2,3,4]) == False
        input = "nums = [1,2,3,4]"
        answer = "False"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        assert  Array._0217_contains_duplicate(nums = [1,1,1,3,3,4,3,2,4,2]) == True
        input = "nums = [1,1,1,3,3,4,3,2,4,2]"
        answer = "True"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _0219_contains_duplicate_II(self) -> None:
        #   | Case 1
        assert  Array._0219_contains_duplicate_II(nums = [1,2,3,1], k = 3) == True
        input = "nums = [1,2,3,1], k = 3"
        answer = "True"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        assert  Array._0219_contains_duplicate_II(nums = [1,0,1,1], k = 1) == True
        input = "nums = [1,0,1,1], k = 1"
        answer = "True"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        assert  Array._0219_contains_duplicate_II(nums = [1,2,3,1,2,3], k = 2) == False
        input = "nums = [1,2,3,1,2,3], k = 2"
        answer = "False"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _0242_valid_anagram(self) -> None:
        #   | Case 1
        assert Array._0242_valid_anagram(s = "anagram", t = "nagaram") == True
        input = 's = "anagram", t = "nagaram"'
        answer = True
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        assert Array._0242_valid_anagram(s = "rat", t = "car") == False
        input = 's = "rat", t = "car"'
        answer = False
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _0940_fruit_into_baskets(self) -> None:
        #   | Case 1
        assert  Array._0940_fruit_into_baskets(fruits = [1,2,1]) == 3
        input = "fruits = [1,2,1]"
        answer = "3"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        assert  Array._0940_fruit_into_baskets(fruits = [0,1,2,2]) == 3
        input = "fruits = [0,1,2,2]"
        answer = "3"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        assert  Array._0940_fruit_into_baskets(fruits = [1,2,3,2,2]) == 4
        input = "fruits = [1,2,3,2,2]"
        answer = "4"
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