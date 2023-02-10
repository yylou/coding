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
    def __init__(self) -> None:
        pass

    @classmethod
    def run(self, *values, **options):
        # Array
        function = Array.search(values[0]).__func__
        if function:
            options["self"] = Array
            if   values[0] == "0027": function(**options); print(options["nums"])
            elif values[0] == "0088": function(**options); print(options["nums1"])
            else: print(function(**options))

    @classmethod
    def search(self, id: str):
        for key, function in self.__dict__.items():
            if key[1:5] == id: function.__func__(self)
        return None

    @classmethod
    def _0027_remove_element(self) -> None:
        func = Array._0027_remove_element

        #   | Case 1
        nums, val = [3,2,2,3], 3
        assert func(nums=nums, val=val) == 2
        assert val not in set(nums[:2]), f"Key value not being removed: {nums}"
        input = 'nums = [3,2,2,3], val = 3'
        answer = 2
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}, {nums[:answer]}")

        #   | Case 2
        nums, val = [0,1,2,2,3,0,4,2], 2
        assert func(nums=nums, val=val) == 5
        assert val not in set(nums[:5]), f"Key value not being removed: {nums}"
        input = 'nums = [0,1,2,2,3,0,4,2], val = 2'
        answer = 5
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}, {nums[:answer]}\n")
    
    @classmethod
    def _0049_group_anagrams(self) -> None:
        func = Array._0049_group_anagrams

        #   | Case 1
        answer = set(list(map(tuple, [sorted(["bat"]),sorted(["nat","tan"]),sorted(["ate","eat","tea"])])))
        diff = len(set(list(map(tuple, [sorted(_) for _ in func(strs = ["eat","tea","tan","ate","nat","bat"])]))).difference(answer))
        assert diff == 0
        input = 'strs = ["eat","tea","tan","ate","nat","bat"]'
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        answer = set(list(map(tuple, [[""]])))
        diff = len(set(list(map(tuple, [sorted(_) for _ in func(strs = [""])]))).difference(answer))
        assert diff == 0
        input = 'strs = [""]'
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        answer = set(list(map(tuple, [["a"]])))
        diff = len(set(list(map(tuple, [sorted(_) for _ in func(strs = ["a"])]))).difference(answer))
        assert diff == 0
        input = 'strs = ["a"]'
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

    @classmethod
    def _0088_merge_sorted_array(self) -> None:
        func = Array._0088_merge_sorted_array

        #   | Case 1
        nums1 = [1,2,3,0,0,0]
        func(nums1 = nums1, m = 3, nums2 = [2,5,6], n = 3)
        answer = [1,2,2,3,5,6]
        assert nums1 == answer
        input = "nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        nums1 = [1]
        func(nums1 = nums1, m = 1, nums2 = [], n = 0)
        answer = [1]
        assert nums1 == answer
        input = "nums1 = [1], m = 1, nums2 = [], n = 0"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        nums1 = [0]
        Array._0088_merge_sorted_array(nums1 = nums1, m = 0, nums2 = [1], n = 1)
        answer = [1]
        assert nums1 == answer
        input = "nums1 = [0], m = 0, nums2 = [1], n = 1"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _0121_best_time_buy_sell_stock(self) -> None:
        func = Array._0121_best_time_buy_sell_stock

        #   | Case 1
        answer = 5
        assert func(prices = [7,1,5,3,6,4]) == answer
        input = "prices = [7,1,5,3,6,4]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        answer = 0
        assert func(prices = [7,6,4,3,1]) == answer
        input = "prices = [7,6,4,3,1]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _0122_best_time_buy_sell_stock_II(self) -> None:
        func = Array._0122_best_time_buy_sell_stock_II

        #   | Case 1
        answer = 7
        assert func(prices = [7,1,5,3,6,4]) == answer
        input = "prices = [7,1,5,3,6,4]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        answer = 4
        assert func(prices = [1,2,3,4,5]) == answer
        input = "prices = [1,2,3,4,5]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        answer = 0
        assert func(prices = [7,6,4,3,1]) == answer
        input = "prices = [7,6,4,3,1]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _0217_contains_duplicate(self) -> None:
        func = Array._0217_contains_duplicate
        
        #   | Case 1
        answer = True
        assert  func(nums = [1,2,3,1]) == answer
        input = "nums = [1,2,3,1]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        answer = False
        assert  func(nums = [1,2,3,4]) == answer
        input = "nums = [1,2,3,4]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        answer = True
        assert  func(nums = [1,1,1,3,3,4,3,2,4,2]) == answer
        input = "nums = [1,1,1,3,3,4,3,2,4,2]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _0219_contains_duplicate_II(self) -> None:
        func = Array. _0219_contains_duplicate_II

        #   | Case 1
        answer = True
        assert  func(nums = [1,2,3,1], k = 3) == answer
        input = "nums = [1,2,3,1], k = 3"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        answer = True
        assert  func(nums = [1,0,1,1], k = 1) == answer
        input = "nums = [1,0,1,1], k = 1"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        answer = False
        assert  func(nums = [1,2,3,1,2,3], k = 2) == answer
        input = "nums = [1,2,3,1,2,3], k = 2"
        answer = "False"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _0242_valid_anagram(self) -> None:
        func =  Array._0242_valid_anagram

        #   | Case 1
        answer = True
        assert func(s = "anagram", t = "nagaram") == answer
        input = 's = "anagram", t = "nagaram"'
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        answer = False
        assert func(s = "rat", t = "car") == answer
        input = 's = "rat", t = "car"'
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _0940_fruit_into_baskets(self) -> None:
        func = Array._0940_fruit_into_baskets
        
        #   | Case 1
        answer = 3
        assert  func(fruits = [1,2,1]) == answer
        input = "fruits = [1,2,1]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        answer = 3
        assert  func(fruits = [0,1,2,2]) == answer
        input = "fruits = [0,1,2,2]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        answer = 4
        assert  func(fruits = [1,2,3,2,2]) == answer
        input = "fruits = [1,2,3,2,2]"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _1470_shuffle_array(self) -> None:
        func = Array._1470_shuffle_array

        #   | Case 1
        answer = [2,3,5,4,1,7]
        assert func(nums = [2,5,1,3,4,7], n = 3) == answer
        input = "nums = [2,5,1,3,4,7], n = 3"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        answer = [1,4,2,3,3,2,4,1]
        assert func(nums = [1,2,3,4,4,3,2,1], n = 4) == answer
        input = "nums = [1,2,3,4,4,3,2,1], n = 4"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        answer = [1,2,1,2]
        assert func(nums = [1,1,2,2], n = 2) == answer
        input = "nums = [1,1,2,2], n = 2"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")