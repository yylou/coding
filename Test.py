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

class Colors:
    END   = "\033[0m"

    # Feature
    NORM  = "0"
    BOLD  = "1"
    TRANS = "3"
    LINE  = "4"
    REV   = "7"
    DEL   = "9"
    NONE  = "8"

    # Text
    TWHITE   = "0"
    TBLACK   = "30"
    TRED     = "31"
    TGREEN   = "32"
    TYELLOW  = "33"
    TBLUE    = "34"
    TPURPLE  = "35"
    TCYAN    = "36"
    TGREY    = "37"
    TDGREY   = "90"
    TLRED    = "91"
    TLGREEN  = "92"
    TLYELLOW = "93"
    TLBLUE   = "94"
    TLPURPLE = "95"
    TLCYAN   = "96"

    # Background
    BNONE    = "10"
    BBLACK   = "40"
    BRED     = "41"
    BGREEN   = "42"
    BYELLOW  = "43"
    BBLUE    = "44"
    BPURPLE  = "45"
    BCYAN    = "46"
    BLGREY   = "47"

    def Pattern(feature, text, background):
        """
        Return the color pattern.

        args:
            @feature:       str
            @text:          str
            @background:    str
        """

        return "\033[{0};{1};{2}m".format(feature, text, background)

class Test:

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
            if key[1:5] == id: function.__func__(self); break
        else: print("    No test data")

    @ classmethod
    def check(self, input, submit, answer):
        assert submit == answer, f"{submit}\nAnswer: {answer}"
        YELLOW = Colors.Pattern(Colors.NORM, Colors.TYELLOW, Colors.BNONE)
        END    = Colors.END
        print(f"\n{YELLOW}    [Input]     {input}{END}")
        print(f"{YELLOW}    [Answer]    {answer}{END}")

    # ---

    @classmethod
    def _0027_remove_element(self) -> None:
        func = Array._0027_remove_element

        #   | Case 1
        input = 'nums = [3,2,2,3], val = 3'
        nums, val = [3,2,2,3], 3
        submit = func(nums=nums, val=val)
        answer = 2
        assert submit == answer, f"{submit}\nAnswer: {answer}"
        assert val not in set(nums[:2]), f"Key value not being removed: {nums}"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}, {nums[:answer]}")

        #   | Case 2
        input = 'nums = [0,1,2,2,3,0,4,2], val = 2'
        nums, val = [0,1,2,2,3,0,4,2], 2
        submit = func(nums=nums, val=val)
        answer = 5
        assert submit == answer, f"{submit}\nAnswer: {answer}"
        assert val not in set(nums[:5]), f"Key value not being removed: {nums}"
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}, {nums[:answer]}\n")
    
    @classmethod
    def _0045_jump_game_II(self) -> None:
        func = Array._0045_jump_game_II

        #   | Case 1
        input  = 'nums = [2,3,1,1,4]'
        submit = func(nums = [2,3,1,1,4])
        answer = 2
        self.check(input, submit, answer)

        #   | Case 2
        input  = 'nums = [2,3,0,1,4]'
        submit = func(nums = [2,3,0,1,4])
        answer = 2
        self.check(input, submit, answer)

    @classmethod
    def _0055_jump_game(self) -> None:
        func = Array._0055_jump_game

        #   | Case 1
        input  = 'nums = [2,3,1,1,4]'
        submit = func(nums = [2,3,1,1,4])
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input  = 'nums = [3,2,1,0,4]'
        submit = func(nums = [3,2,1,0,4])
        answer = False
        self.check(input, submit, answer)

    @classmethod
    def _0049_group_anagrams(self) -> None:
        func = Array._0049_group_anagrams

        #   | Case 1
        input  = 'strs = ["eat","tea","tan","ate","nat","bat"]'
        submit = func(strs = ["eat","tea","tan","ate","nat","bat"])
        answer = set(list(map(tuple, [sorted(["bat"]),sorted(["nat","tan"]),sorted(["ate","eat","tea"])])))
        diff = len(set(list(map(tuple, [sorted(_) for _ in submit]))).difference(answer))
        assert diff == 0
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 2
        input  = 'strs = [""]'
        submit = func(strs = [""])
        answer = [[""]]
        diff = len(set(list(map(tuple, [sorted(_) for _ in submit]))).difference(set(list(map(tuple, answer)))))
        assert diff == 0
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        input = 'strs = ["a"]'
        submit = func(strs = ["a"])
        answer = [["a"]]
        diff = len(set(list(map(tuple, [sorted(_) for _ in submit]))).difference(set(list(map(tuple, answer)))))
        assert diff == 0
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}\n")

    @classmethod
    def _0088_merge_sorted_array(self) -> None:
        func = Array._0088_merge_sorted_array

        #   | Case 1
        input = "nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3"
        nums1 = [1,2,3,0,0,0]
        func(nums1 = nums1, m = 3, nums2 = [2,5,6], n = 3)
        submit = nums1
        answer = [1,2,2,3,5,6]
        self.check(input, submit, answer)

        #   | Case 2
        input = "nums1 = [1], m = 1, nums2 = [], n = 0"
        nums1 = [1]
        func(nums1 = nums1, m = 1, nums2 = [], n = 0)
        answer = [1]
        submit = nums1
        self.check(input, submit, answer)

        #   | Case 3
        input = "nums1 = [0], m = 0, nums2 = [1], n = 1"
        nums1 = [0]
        func(nums1 = nums1, m = 0, nums2 = [1], n = 1)
        submit = nums1
        answer = [1]
        self.check(input, submit, answer)

    @classmethod
    def _0121_best_time_buy_sell_stock(self) -> None:
        func = Array._0121_best_time_buy_sell_stock

        #   | Case 1
        input  = "prices = [7,1,5,3,6,4]"
        submit = func(prices = [7,1,5,3,6,4])
        answer = 5
        self.check(input, submit, answer)

        #   | Case 2
        input  = "prices = [7,6,4,3,1]"
        submit = func(prices = [7,6,4,3,1])
        answer = 0
        self.check(input, submit, answer)

    @classmethod
    def _0122_best_time_buy_sell_stock_II(self) -> None:
        func = Array._0122_best_time_buy_sell_stock_II

        #   | Case 1
        input  = "prices = [7,1,5,3,6,4]"
        submit = func(prices = [7,1,5,3,6,4])
        answer = 7
        self.check(input, submit, answer)

        #   | Case 2
        input  = "prices = [1,2,3,4,5]"
        submit = func(prices = [1,2,3,4,5])
        answer = 4
        assert submit == answer
        print(f"\n    [Input]     {input}")
        print(f"    [Answer]    {answer}")

        #   | Case 3
        input  = "prices = [7,6,4,3,1]"
        submit = func(prices = [7,6,4,3,1])
        answer = 0
        self.check(input, submit, answer)

    @classmethod
    def _0217_contains_duplicate(self) -> None:
        func = Array._0217_contains_duplicate
        
        #   | Case 1
        input  = "nums = [1,2,3,1]"
        submit = func(nums = [1,2,3,1])
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input  = "nums = [1,2,3,4]"
        submit = func(nums = [1,2,3,4])
        answer = False
        self.check(input, submit, answer)

        #   | Case 3
        input  = "nums = [1,1,1,3,3,4,3,2,4,2]"
        submit = func(nums = [1,1,1,3,3,4,3,2,4,2])
        answer = True
        self.check(input, submit, answer)

    @classmethod
    def _0219_contains_duplicate_II(self) -> None:
        func = Array. _0219_contains_duplicate_II

        #   | Case 1
        input  = "nums = [1,2,3,1], k = 3"
        submit = func(nums = [1,2,3,1], k = 3)
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input  = "nums = [1,0,1,1], k = 1"
        answer = True
        submit = func(nums = [1,0,1,1], k = 1)
        self.check(input, submit, answer)

        #   | Case 3
        input  = "nums = [1,2,3,1,2,3], k = 2"
        submit =  func(nums = [1,2,3,1,2,3], k = 2)
        answer = False
        self.check(input, submit, answer)

    @classmethod
    def _0238_product_of_array_except_self(self) -> None:
        func =  Array._0238_product_of_array_except_self

        #   | Case 1
        input  = 'nums = [1,2,3,4]'
        submit = func(nums = [1,2,3,4])
        answer = [24,12,8,6]
        self.check(input, submit, answer)

        #   | Case 2
        input  = 'nums = [-1,1,0,-3,3]'
        submit = func(nums = [-1,1,0,-3,3])
        answer = [0,0,9,0,0]
        self.check(input, submit, answer)

    @classmethod
    def _0242_valid_anagram(self) -> None:
        func =  Array._0242_valid_anagram

        #   | Case 1
        input  = 's = "anagram", t = "nagaram"'
        submit = func(s = "anagram", t = "nagaram")
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input  = 's = "rat", t = "car"'
        submit = func(s = "rat", t = "car")
        answer = False
        self.check(input, submit, answer)

    @classmethod
    def _0940_fruit_into_baskets(self) -> None:
        func = Array._0940_fruit_into_baskets
        
        #   | Case 1
        input  = "fruits = [1,2,1]"
        submit = func(fruits = [1,2,1])
        answer = 3
        self.check(input, submit, answer)

        #   | Case 2
        input  = "fruits = [0,1,2,2]"
        submit = func(fruits = [0,1,2,2])
        answer = 3
        self.check(input, submit, answer)

        #   | Case 3
        input  = "fruits = [1,2,3,2,2]"
        submit = func(fruits = [1,2,3,2,2])
        answer = 4
        self.check(input, submit, answer)

    @classmethod
    def _1470_shuffle_array(self) -> None:
        func = Array._1470_shuffle_array

        #   | Case 1
        input  = "nums = [2,5,1,3,4,7], n = 3"
        submit = func(nums = [2,5,1,3,4,7], n = 3)
        answer = [2,3,5,4,1,7]
        self.check(input, submit, answer)

        #   | Case 2
        input  = "nums = [1,2,3,4,4,3,2,1], n = 4"
        submit = func(nums = [1,2,3,4,4,3,2,1], n = 4)
        answer = [1,4,2,3,3,2,4,1]
        assert submit == answer
        self.check(input, submit, answer)

        #   | Case 3
        input  = "nums = [1,1,2,2], n = 2"
        submit = func(nums = [1,1,2,2], n = 2)
        answer = [1,2,1,2]
        self.check(input, submit, answer)