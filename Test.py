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
from String                     import String
from Stack                      import Stack
from Tree                       import Tree, TreeNode

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

    YELLOW = Colors.Pattern(Colors.NORM, Colors.TYELLOW, Colors.BNONE)
    END    = Colors.END

    @classmethod
    def run(self, *values, **options):
        array  = Array.search(values[0])
        string = String.search(values[0])
        stack  = Stack.search(values[0])
        tree   = Tree.search(values[0])
        
        if array:
            func = array.__func__
            options["self"] = Array
            if   values[0] == "0027": func(**options); print(options["nums"])
            elif values[0] == "0088": func(**options); print(options["nums1"])
            else: print(func(**options))

        elif string:
            func = string.__func__
            options["self"] = String
            print(function(**options))

        elif stack:
            func = stack.__func__
            options["self"] = Stack
            print(function(**options))
        
        elif tree:
            func = tree.__func__
            options["self"] = Tree
            print(function(**options))

    @classmethod
    def search(self, id: str, obj: object, func: object):
        for key, function in self.__dict__.items():
            if key[1:5] == id: function.__func__(self, obj, func); break
        else: print(f"{self.YELLOW}    No test data{self.END}")

    @classmethod
    def check(self, input, submit, answer):
        assert submit == answer, f"{submit}\nAnswer: {answer}"
        print(f"\n{self.YELLOW}    [Input]     {input}{self.END}")
        print(f"{self.YELLOW}    [Answer]    {answer}{self.END}")

    # ---

    @classmethod
    def _0001_two_sum(self, obj, func) -> None:
        # func = Array._0001_two_sum

        #   | Case 1
        input  = 'nums = [2,7,11,15], target = 9'
        submit = func(obj, nums = [2,7,11,15], target = 9)
        answer = [0,1]
        self.check(input, set(submit), set(answer))

        #   | Case 2
        input  = 'nums = [3,2,4], target = 6'
        submit = func(obj, nums = [3,2,4], target = 6)
        answer = [1,2]
        self.check(input, set(submit), set(answer))

        #   | Case 3
        input  = "nums = [3,3], target = 6"
        submit = func(obj, nums = [3,3], target = 6)
        answer = [0,1]
        self.check(input, set(submit), set(answer))

    @classmethod
    def _0003_longest_substring_without_repeating_characters(self, obj, func) -> None:
        #   | Case 1
        input = 's = "abcabcbb"'
        submit = func(obj, s = "abcabcbb")
        answer = 3
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 2
        input = 's = "bbbbb"'
        submit = func(obj, s = "bbbbb")
        answer = 1
        self.check(input=input, submit=submit, answer=answer)
        
        #   | Case 3
        input = 's = "pwwkew"'
        submit = func(obj, s = "pwwkew")
        answer = 3
        self.check(input=input, submit=submit, answer=answer)  

    @classmethod
    def _0011_container_with_most_water(self, obj, func) -> None:
        #   | Case 1
        input  = 'height = [1,8,6,2,5,4,8,3,7]'
        submit = func(obj, height = [1,8,6,2,5,4,8,3,7])
        answer = 49
        self.check(input, submit, answer)

        #   | Case 2
        input  = 'height = [1,1]'
        submit = func(obj, height = [1,1])
        answer = 1
        self.check(input, submit, answer)

    @classmethod
    def _0015_3sum(self, obj, func) -> None:
        #   | Case 1
        input = 'nums = [-1,0,1,2,-1,-4]'
        submit = func(obj, nums = [-1,0,1,2,-1,-4])
        answer = [[-1,-1,2],[-1,0,1]]
        self.check(input=input, submit=set(submit), answer=set(map(tuple, answer)))

        #   | Case 2
        input = 'nums = [0,1,1]'
        submit = func(obj, nums = [0,1,1])
        answer = []
        self.check(input=input, submit=set(submit), answer=set(map(tuple, answer)))

        #   | Case 3
        input = 'nums = [0,0,0]'
        submit = func(obj, nums = [0,0,0])
        answer = [[0,0,0]]
        self.check(input=input, submit=set(submit), answer=set(map(tuple, answer)))

    @classmethod
    def _0020_valid_parentheses(self, obj, func) -> None:
        #   | Case 1
        input = 's = "()"'
        submit = func(obj, s = "()")
        answer = True
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 2
        input = 's = "()[]{}"'
        submit = func(obj, s = "()[]{}")
        answer = True
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 3
        input = 's = "(]"'
        submit = func(obj, s = "(]")
        answer = False
        self.check(input=input, submit=submit, answer=answer)

    @classmethod
    def _0022_generate_parentheses(self, obj, func) -> None:
        #   | Case 1
        input = 'n = 3'
        submit = func(obj, n = 3)
        answer = ["((()))","(()())","(())()","()(())","()()()"]
        self.check(input=input, submit=set(submit), answer=set(answer))

        #   | Case 2
        input = 'n = 1'
        submit = func(obj, n = 1)
        answer = ["()"]
        self.check(input=input, submit=set(submit), answer=set(answer))

    @classmethod
    def _0027_remove_element(self, obj, func) -> None:
        #   | Case 1
        input = 'nums = [3,2,2,3], val = 3'
        nums, val = [3,2,2,3], 3
        submit = func(obj, nums=nums, val=val)
        answer = 2
        assert submit == answer, f"{submit}\nAnswer: {answer}"
        assert val not in set(nums[:2]), f"Key value not being removed: {nums}"
        print(f"\n{self.YELLOW}    [Input]     {input}{self.END}")
        print(f"{self.YELLOW}    [Answer]    {answer}, {nums[:answer]}{self.END}")

        #   | Case 2
        input = 'nums = [0,1,2,2,3,0,4,2], val = 2'
        nums, val = [0,1,2,2,3,0,4,2], 2
        submit = func(obj, nums=nums, val=val)
        answer = 5
        assert submit == answer, f"{submit}\nAnswer: {answer}"
        assert val not in set(nums[:5]), f"Key value not being removed: {nums}"
        print(f"\n{self.YELLOW}    [Input]     {input}{self.END}")
        print(f"{self.YELLOW}    [Answer]    {answer}, {nums[:answer]}{self.END}")
    
    @classmethod
    def _0028_find_the_index_of_the_first_occurence_in_a_string(self, obj, func) -> None:
        #   | Case 1
        input = ""
        submit = func(obj, )
        answer = ""
        self.check(input=input, submit=submit, answer=answer)

    @classmethod
    def _0033_search_in_rotated_sorted_array(self, obj, func) -> None:
        #   | Case 1
        input = 'nums = [4,5,6,7,0,1,2], target = 0'
        submit = func(obj, nums = [4,5,6,7,0,1,2], target = 0)
        answer = 4
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 2
        input = 'nums = [4,5,6,7,0,1,2], target = 3'
        submit = func(obj, nums = [4,5,6,7,0,1,2], target = 3)
        answer = -1
        self.check(input=input, submit=submit, answer=answer)
        
        #   | Case 3
        input = 'nums = [1], target = 0'
        submit = func(obj, nums = [1], target = 0)
        answer = -1
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 4
        input = 'nums = [1,2,3], target = 1'
        submit = func(obj, nums = [1,2,3], target = 1)
        answer = 0
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 5
        input = 'nums = [1], target = 1'
        submit = func(obj, nums = [1], target = 1)
        answer = 0
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 6
        input = 'nums = [1,3], target = 1'
        submit = func(obj, nums = [1,2,3], target = 1)
        answer = 0
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 7
        input = 'nums = [3,5,1], target = 3'
        submit = func(obj, nums = [3,5,1], target = 3)
        answer = 0
        self.check(input=input, submit=submit, answer=answer)

    @classmethod
    def _0036_valid_sudoku(self, obj, func) -> None:

        #   | Case 1
        input  = 'board = [ ["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]]'
        submit = func(obj, board = [ ["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]])
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input  = 'board = [ ["8","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]]'
        submit = func(obj, board = [ ["8","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]])
        answer = False
        self.check(input, submit, answer)

    @classmethod
    def _0045_jump_game_II(self, obj, func) -> None:
        #   | Case 1
        input  = 'nums = [2,3,1,1,4]'
        submit = func(obj, nums = [2,3,1,1,4])
        answer = 2
        self.check(input, submit, answer)

        #   | Case 2
        input  = 'nums = [2,3,0,1,4]'
        submit = func(obj, nums = [2,3,0,1,4])
        answer = 2
        self.check(input, submit, answer)

    @classmethod
    def _0049_group_anagrams(self, obj, func) -> None:
        #   | Case 1
        input  = 'strs = ["eat","tea","tan","ate","nat","bat"]'
        submit = func(obj, strs = ["eat","tea","tan","ate","nat","bat"])
        answer = set(list(map(tuple, [sorted(["bat"]),sorted(["nat","tan"]),sorted(["ate","eat","tea"])])))
        diff = len(set(list(map(tuple, [sorted(_) for _ in submit]))).difference(answer))
        assert diff == 0
        print(f"\n{self.YELLOW}    [Input]     {input}{self.END}")
        print(f"{self.YELLOW}    [Answer]    {answer}{self.END}")

        #   | Case 2
        input  = 'strs = [""]'
        submit = func(obj, strs = [""])
        answer = [[""]]
        diff = len(set(list(map(tuple, [sorted(_) for _ in submit]))).difference(set(list(map(tuple, answer)))))
        assert diff == 0
        print(f"\n{self.YELLOW}    [Input]     {input}{self.END}")
        print(f"{self.YELLOW}    [Answer]    {answer}{self.END}")

        #   | Case 3
        input = 'strs = ["a"]'
        submit = func(obj, strs = ["a"])
        answer = [["a"]]
        diff = len(set(list(map(tuple, [sorted(_) for _ in submit]))).difference(set(list(map(tuple, answer)))))
        assert diff == 0
        print(f"\n{self.YELLOW}    [Input]     {input}{self.END}")
        print(f"{self.YELLOW}    [Answer]    {answer}{self.END}")

    @classmethod
    def _0053_maximum_subarray(self, obj, func) -> None:
        #   | Case 1
        input = 'nums = [-2,1,-3,4,-1,2,1,-5,4]'
        submit = func(obj, nums = [-2,1,-3,4,-1,2,1,-5,4])
        answer = 6
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 2
        input = 'nums = [1]'
        submit = func(obj, nums = [1])
        answer = 1
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 3
        input = 'nums = [5,4,-1,7,8]'
        submit = func(obj, nums = [5,4,-1,7,8])
        answer = 23
        self.check(input=input, submit=submit, answer=answer)

    @classmethod
    def _0055_jump_game(self, obj, func) -> None:
        #   | Case 1
        input  = 'nums = [2,3,1,1,4]'
        submit = func(obj, nums = [2,3,1,1,4])
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input  = 'nums = [3,2,1,0,4]'
        submit = func(obj, nums = [3,2,1,0,4])
        answer = False
        self.check(input, submit, answer)

    @classmethod
    def _0056_merge_intervals(self, obj, func) -> None:
        #   | Case 1
        input = 'intervals = [[1,3],[2,6],[8,10],[15,18]]'
        submit = func(obj, intervals = [[1,3],[2,6],[8,10],[15,18]])
        answer = [[1,6],[8,10],[15,18]]
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 2
        input = 'intervals = [[1,4],[4,5]]'
        submit = func(obj, intervals = [[1,4],[4,5]])
        answer = [[1,5]]
        self.check(input=input, submit=submit, answer=answer)

    @classmethod
    def _0088_merge_sorted_array(self, obj, func) -> None:
        #   | Case 1
        input = "nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3"
        nums1 = [1,2,3,0,0,0]
        func(obj, nums1 = nums1, m = 3, nums2 = [2,5,6], n = 3)
        submit = nums1
        answer = [1,2,2,3,5,6]
        self.check(input, submit, answer)

        #   | Case 2
        input = "nums1 = [1], m = 1, nums2 = [], n = 0"
        nums1 = [1]
        func(obj, nums1 = nums1, m = 1, nums2 = [], n = 0)
        answer = [1]
        submit = nums1
        self.check(input, submit, answer)

        #   | Case 3
        input = "nums1 = [0], m = 0, nums2 = [1], n = 1"
        nums1 = [0]
        func(obj, nums1 = nums1, m = 0, nums2 = [1], n = 1)
        submit = nums1
        answer = [1]
        self.check(input, submit, answer)

    @classmethod
    def _0098_validate_BST(self, obj, func) -> None:
        #   | Case 1
        input = TreeNode(2)
        input.left = TreeNode(1)
        input.right = TreeNode(3)
        _input = str(input)
        submit = func(obj, input)
        answer = True
        self.check(input=_input, submit=submit, answer=answer)

        #   | Case 2
        input = TreeNode(5)
        input.left = TreeNode(1)
        input.right = TreeNode(4)
        input.right.left = TreeNode(3)
        input.right.right = TreeNode(6)
        _input = str(input)
        submit = func(obj, input)
        answer = False
        self.check(input=_input, submit=submit, answer=answer)

        #   | Case 3
        input = TreeNode(5)
        input.left = TreeNode(4)
        input.right = TreeNode(6)
        input.right.left = TreeNode(3)
        input.right.right = TreeNode(7)
        _input = str(input)
        submit = func(obj, input)
        answer = False
        self.check(input=_input, submit=submit, answer=answer)

    @classmethod
    def _0100_same_tree(self, obj, func) -> None:
        #   | Case 1
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        input = root
        submit = func(obj, input, input)
        answer = True
        self.check(f"{input}\n                {input}", submit, answer)

        #   | Case 2
        p = TreeNode(1)
        p.left = TreeNode(2)
        q = TreeNode(1)
        q.right = TreeNode(2)
        submit = func(obj, p, q)
        answer = False
        self.check(f"{p}\n                {q}", submit, answer)

        #   | Case 2
        p = TreeNode(1)
        p.left  = TreeNode(2)
        p.right = TreeNode(1)
        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)
        submit = func(obj, p, q)
        answer = False
        self.check(f"{p}\n                {q}", submit, answer)

    @classmethod
    def _0102_binary_tree_level_order_traversal(self, obj, func) -> None:
        #   | Case 1
        input = TreeNode(3)
        input.left = TreeNode(9)
        input.right = TreeNode(20)
        input.right.left = TreeNode(15)
        input.right.right = TreeNode(7)
        submit = func(obj, input)
        answer = [[3],[9,20],[15,7]]
        self.check(input, submit, answer)

        #   | Case 2
        input = TreeNode(1)
        submit = func(obj, input)
        answer = [[1]]
        self.check(input, submit, answer)

        #   | Case 3
        input = None
        submit = func(obj, input)
        answer = []
        self.check(input, submit, answer)

    @classmethod
    def _0110_balanced_binary_tree(self, obj, func) -> None:
        #   | Case 1
        input = TreeNode(3)
        input.left  = TreeNode(9)
        input.right = TreeNode(20)
        input.right.left  = TreeNode(20)
        input.right.right = TreeNode(7)
        submit = func(obj, input)
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input = TreeNode(1)
        input.left  = TreeNode(2)
        input.right = TreeNode(2)
        input.left.left  = TreeNode(3)
        input.left.right = TreeNode(3)
        input.left.left.left  = TreeNode(4)
        input.left.left.right = TreeNode(4)
        submit = func(obj, input)
        answer = False
        self.check(input, submit, answer)

        #   | Case 3
        input = None
        submit = func(obj, input)
        answer = True
        self.check(input, submit, answer)

    @classmethod
    def _0121_best_time_buy_sell_stock(self, obj, func) -> None:
        #   | Case 1
        input  = "prices = [7,1,5,3,6,4]"
        submit = func(obj, prices = [7,1,5,3,6,4])
        answer = 5
        self.check(input, submit, answer)

        #   | Case 2
        input  = "prices = [7,6,4,3,1]"
        submit = func(obj, prices = [7,6,4,3,1])
        answer = 0
        self.check(input, submit, answer)

    @classmethod
    def _0122_best_time_buy_sell_stock_II(self, obj, func) -> None:
        #   | Case 1
        input  = "prices = [7,1,5,3,6,4]"
        submit = func(obj, prices = [7,1,5,3,6,4])
        answer = 7
        self.check(input, submit, answer)

        #   | Case 2
        input  = "prices = [1,2,3,4,5]"
        submit = func(obj, prices = [1,2,3,4,5])
        answer = 4
        self.check(input, submit, answer)

        #   | Case 3
        input  = "prices = [7,6,4,3,1]"
        submit = func(obj, prices = [7,6,4,3,1])
        answer = 0
        self.check(input, submit, answer)

    @classmethod
    def _0125_valid_palindrome(self, obj, func) -> None:
        #   | Case 1
        input  = 's = "A man, a plan, a canal: Panama"'
        submit = func(obj, s = "A man, a plan, a canal: Panama")
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input  = 's = "race a car"'
        submit = func(obj, s = "race a car")
        answer = False
        self.check(input, submit, answer)

        #   | Case 3
        input  = " "
        submit = func(obj, s = " ")
        answer = True
        self.check(input, submit, answer)

    @classmethod
    def _0152_maximum_product_subarray(self, obj, func) -> None:
        #   | Case 1
        input = 'nums = [2,3,-2,4]'
        submit = func(obj, nums = [2,3,-2,4])
        answer = 6
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 2
        input = 'nums = [-2,0,-1]'
        submit = func(obj, nums = [-2,0,-1])
        answer = 0
        self.check(input=input, submit=submit, answer=answer)

    @classmethod
    def _0153_find_minimum_in_rotated_sorted_array(self, obj, func) -> None:
        #   | Case 1
        input = 'nums = [4,5,6,7,0,1,2]'
        submit = func(obj, nums = [4,5,6,7,0,1,2])
        answer = 0
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 2
        input = 'nums = [3,4,5,1,2]'
        submit = func(obj, nums = [3,4,5,1,2])
        answer = 1
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 4
        input = 'nums = [11,13,15,17]'
        submit = func(obj, nums = [11,13,15,17])
        answer = 11
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 5
        input = 'nums = [2,1]'
        submit = func(obj, nums = [2,1])
        answer = 1
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 6
        input = 'nums = [3,1,2]'
        submit = func(obj, nums = [3,1,2])
        answer = 1
        self.check(input=input, submit=submit, answer=answer)

    @classmethod
    def _0155_min_stack(self, obj, func) -> None:
        #   | Case 1
        input  = 'push(-2), push(0), push(-3), getMin, pop, top, getMin'
        submit = func(obj)
        answer = [None, None, None, -3, None, 0, -2]
        self.check(input, submit, answer)

    @classmethod
    def _0167_two_sum_II_input_array_sorted(self, obj, func) -> None:
        #   | Case 1
        input = "numbers = [2,7,11,15], target = 9"
        submit = func(obj, numbers = [2,7,11,15], target = 9)
        answer = [1, 2]
        self.check(input, set(submit), set(answer))

        #   | Case 2
        input = "numbers = [2,3,4], target = 6"
        submit = func(obj, numbers = [2,3,4], target = 6)
        answer = [1, 3]
        self.check(input, set(submit), set(answer))

        #   | Case 3
        input = "numbers = [-1,0], target = -1"
        submit = func(obj, numbers = [-1,0], target = -1)
        answer = [1, 2]
        self.check(input, set(submit), set(answer))

    @classmethod
    def _0217_contains_duplicate(self, obj, func) -> None:
        #   | Case 1
        input  = "nums = [1,2,3,1]"
        submit = func(obj, nums = [1,2,3,1])
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input  = "nums = [1,2,3,4]"
        submit = func(obj, nums = [1,2,3,4])
        answer = False
        self.check(input, submit, answer)

        #   | Case 3
        input  = "nums = [1,1,1,3,3,4,3,2,4,2]"
        submit = func(obj, nums = [1,1,1,3,3,4,3,2,4,2])
        answer = True
        self.check(input, submit, answer)

    @classmethod
    def _0219_contains_duplicate_II(self, obj, func) -> None:
        #   | Case 1
        input  = "nums = [1,2,3,1], k = 3"
        submit = func(obj, nums = [1,2,3,1], k = 3)
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input  = "nums = [1,0,1,1], k = 1"
        answer = True
        submit = func(obj, nums = [1,0,1,1], k = 1)
        self.check(input, submit, answer)

        #   | Case 3
        input  = "nums = [1,2,3,1,2,3], k = 2"
        submit =  func(obj, nums = [1,2,3,1,2,3], k = 2)
        answer = False
        self.check(input, submit, answer)

    @classmethod
    def _0226_invert_BST(self, obj, func) -> None:
        #   | Case 1
        input = TreeNode(4)
        input.left  = TreeNode(2)
        input.left.left  = TreeNode(1)
        input.left.right = TreeNode(3)
        input.right = TreeNode(7)
        input.right.left  = TreeNode(6)
        input.right.right = TreeNode(9)
        submit = func(obj, root = input)
        answer = [[4], [7, 2], [9, 6, 3, 1]]
        self.check(str(input), str(submit), str(answer))

    @classmethod
    def _0236_lowest_common_ancestor_of_a_binary_tree(self, obj, func) -> None:
        #   | Tree
        root = TreeNode(3)
        root.left  = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left  = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left  = TreeNode(0)
        root.right.right = TreeNode(8)
        root.left.right.left  = TreeNode(7)
        root.left.right.right = TreeNode(4)

        #   | Case 1
        input = root
        submit = func(obj, root = input, p = 5, q = 1)
        answer = 3
        self.check(input=f"{input}, p=5, q=1", submit=submit.val, answer=answer)

        #   | Case 2
        input = root
        submit = func(obj, root = input, p = 5, q = 4)
        answer = 5
        self.check(input=f"{input}, p=5, q=4", submit=submit.val, answer=answer)
        
    @classmethod
    def _0238_product_of_array_except_self(self, obj, func) -> None:
        #   | Case 1
        input  = 'nums = [1,2,3,4]'
        submit = func(obj, nums = [1,2,3,4])
        answer = [24,12,8,6]
        self.check(input, submit, answer)

        #   | Case 2
        input  = 'nums = [-1,1,0,-3,3]'
        submit = func(obj, nums = [-1,1,0,-3,3])
        answer = [0,0,9,0,0]
        self.check(input, submit, answer)

    @classmethod
    def _0242_valid_anagram(self, obj, func) -> None:
        #   | Case 1
        input  = 's = "anagram", t = "nagaram"'
        submit = func(obj, s = "anagram", t = "nagaram")
        answer = True
        self.check(input, submit, answer)

        #   | Case 2
        input  = 's = "rat", t = "car"'
        submit = func(obj, s = "rat", t = "car")
        answer = False
        self.check(input, submit, answer)

    @classmethod
    def _0347_top_k_frequent_elements(self, obj, func) -> None:
        #   | Case 1
        input  = "nums = [1,1,1,2,2,3], k = 2"
        submit = func(obj, nums = [1,1,1,2,2,3], k = 2)
        answer = [1,2]
        self.check(input, sorted(submit), answer)

        #   | Case 2
        input  = "nums = [1], k = 1"
        submit = func(obj, nums = [1], k = 1)
        answer = [1]
        self.check(input, submit, answer)

    @classmethod
    def _0395_longest_substring_with_at_least_k_repeating_characters(self, obj, func) -> None:
        #   | Case 1
        input = 's = "aaabb", k = 3'
        submit = func(obj, s = "aaabb", k = 3)
        answer = 3
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 2
        input = 's = "ababbc", k = 2'
        submit = func(obj, s = "ababbc", k = 2)
        answer = 5
        self.check(input=input, submit=submit, answer=answer)

    @classmethod
    def _0424_longest_repeating_character_replacement(self, obj, func) -> None:
        #   | Case 1
        input = 's = "ABAB", k = 2'
        submit = func(obj, s = "ABAB", k = 2)
        answer = 4
        self.check(input=input, submit=submit, answer=answer)

        #   | Case 2
        input = 's = "AABABBA", k = 1'
        submit = func(obj, s = "AABABBA", k = 1)
        answer = 4
        self.check(input=input, submit=submit, answer=answer)

    @classmethod
    def _0450_delete_node_in_a_BST(self, obj, func) -> None:
        #   | Case 1
        root = TreeNode(5)
        obj._0701_insert_into_a_BST(root, 3)
        obj._0701_insert_into_a_BST(root, 6)
        obj._0701_insert_into_a_BST(root, 2)
        obj._0701_insert_into_a_BST(root, 4)
        obj._0701_insert_into_a_BST(root, 7)
        input = root
        submit = func(obj, root = input, key = 3)
        answer = "[[5], [4, 6], [2, None, None, 7]]"
        self.check(input, str(submit), answer)

        #   | Case 2
        root = TreeNode(5)
        obj._0701_insert_into_a_BST(root, 3)
        obj._0701_insert_into_a_BST(root, 6)
        obj._0701_insert_into_a_BST(root, 2)
        obj._0701_insert_into_a_BST(root, 4)
        obj._0701_insert_into_a_BST(root, 7)
        input = root
        submit = func(obj, root = input, key = 0)
        answer = "[[5], [3, 6], [2, 4, None, 7]]"
        self.check(input, str(submit), answer)

        #   | Case 3
        input = None
        submit = func(obj, root = input, key = 0)
        answer = "None"
        self.check(input, str(submit), answer)

        #   | Case 4
        input = TreeNode(0)
        submit = func(obj, root = input, key = 0)
        answer = "None"
        self.check(input, str(submit), answer)

        #   | Case 5
        root = TreeNode(50)
        obj._0701_insert_into_a_BST(root, 30)
        obj._0701_insert_into_a_BST(root, 40)
        obj._0701_insert_into_a_BST(root, 70)
        obj._0701_insert_into_a_BST(root, 60)
        obj._0701_insert_into_a_BST(root, 80)
        input = root
        submit = func(obj, root = input, key = 50)
        answer = "[[70], [60, 80], [30, None, None, None], [None, 40]]"
        self.check(input, str(submit), answer)

    @classmethod
    def _0502_IPO(self, obj, func) -> None:
        #   | Case 1
        input  = "k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]"
        submit = func(obj, k = 2, w = 0, profits = [1,2,3], capital = [0,1,1])
        answer = 4
        self.check(input, submit, answer)

        #   | Case 2
        input  = "k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]"
        submit = func(obj, k = 3, w = 0, profits = [1,2,3], capital = [0,1,2])
        answer = 6
        self.check(input, submit, answer)

    @classmethod
    def _0530_min_abs_diff_in_BST(self, obj, func) -> None:
        #   | Case 1
        input = TreeNode(4)
        obj._0701_insert_into_a_BST(input, 2)
        obj._0701_insert_into_a_BST(input, 6)
        obj._0701_insert_into_a_BST(input, 1)
        obj._0701_insert_into_a_BST(input, 3)
        submit = func(obj, input)
        answer = 1
        self.check(input, submit, answer)

        #   | Case 2
        input = TreeNode(1)
        obj._0701_insert_into_a_BST(input, 0)
        obj._0701_insert_into_a_BST(input, 48)
        obj._0701_insert_into_a_BST(input, 12)
        obj._0701_insert_into_a_BST(input, 49)
        submit = func(obj, input)
        answer = 1
        self.check(input, submit, answer)

    @classmethod
    def _0700_search_in_a_BST(self, obj, func) -> None:
        #   | Case 1
        root = TreeNode(4)
        obj._0701_insert_into_a_BST(root, 2)
        obj._0701_insert_into_a_BST(root, 7)
        obj._0701_insert_into_a_BST(root, 1)
        obj._0701_insert_into_a_BST(root, 3)
        input = root
        submit = func(obj, root = input, val = 2)
        answer = "[[2], [1, 3]]"
        self.check(input, str(submit), answer)

        #   | Case 2
        root = TreeNode(4)
        obj._0701_insert_into_a_BST(root, 2)
        obj._0701_insert_into_a_BST(root, 7)
        obj._0701_insert_into_a_BST(root, 1)
        obj._0701_insert_into_a_BST(root, 3)
        input = root
        submit = func(obj, root = input, val = 5)
        answer = "None"
        self.check(input, str(submit), answer)

    @classmethod
    def _0701_insert_into_a_BST(self, obj, func) -> None:
        #   | Case 1
        root = TreeNode(4)
        obj._0701_insert_into_a_BST(root, 2)
        obj._0701_insert_into_a_BST(root, 7)
        obj._0701_insert_into_a_BST(root, 1)
        obj._0701_insert_into_a_BST(root, 3)
        input = root
        submit = func(obj, root = input, val = 5)
        answer = "[[4], [2, 7], [1, 3, 5, None]]"
        self.check(input, str(submit), answer)

        #   | Case 2
        root = TreeNode(40)
        obj._0701_insert_into_a_BST(root, 20)
        obj._0701_insert_into_a_BST(root, 60)
        obj._0701_insert_into_a_BST(root, 10)
        obj._0701_insert_into_a_BST(root, 30)
        obj._0701_insert_into_a_BST(root, 50)
        obj._0701_insert_into_a_BST(root, 70)
        input = root
        submit = func(obj, root = input, val = 25)
        answer = "[[40], [20, 60], [10, 30, 50, 70], [None, None, 25, None, None, None, None, None]]"
        self.check(input, str(submit), answer)

    @classmethod
    def _0904_fruit_into_baskets(self, obj, func) -> None:
        #   | Case 1
        input  = "fruits = [1,2,1]"
        submit = func(obj, fruits = [1,2,1])
        answer = 3
        self.check(input, submit, answer)

        #   | Case 2
        input  = "fruits = [0,1,2,2]"
        submit = func(obj, fruits = [0,1,2,2])
        answer = 3
        self.check(input, submit, answer)

        #   | Case 3
        input  = "fruits = [1,2,3,2,2]"
        submit = func(obj, fruits = [1,2,3,2,2])
        answer = 4
        self.check(input, submit, answer)

    @classmethod
    def _1011_capacity_to_ship_packages_within_d_days(self, obj, func) -> None:
        #   | Case 1
        input  = "weights = [1,2,3,4,5,6,7,8,9,10], days = 5"
        submit = func(obj, weights = [1,2,3,4,5,6,7,8,9,10], days = 5)
        answer = 15
        self.check(input, submit, answer)

        #   | Case 2
        input  = "weights = [3,2,2,4,1,4], days = 3"
        submit = func(obj, weights = [3,2,2,4,1,4], days = 3)
        answer = 6
        self.check(input, submit, answer)

        #   | Case 3
        input  = "weights = [1,2,3,1,1], days = 4"
        submit = func(obj, weights = [1,2,3,1,1], days = 4)
        answer = 3
        self.check(input, submit, answer)

    @classmethod
    def _1470_shuffle_array(self, obj, func) -> None:
        #   | Case 1
        input  = "nums = [2,5,1,3,4,7], n = 3"
        submit = func(obj, nums = [2,5,1,3,4,7], n = 3)
        answer = [2,3,5,4,1,7]
        self.check(input, submit, answer)

        #   | Case 2
        input  = "nums = [1,2,3,4,4,3,2,1], n = 4"
        submit = func(obj, nums = [1,2,3,4,4,3,2,1], n = 4)
        answer = [1,4,2,3,3,2,4,1]
        self.check(input, submit, answer)

        #   | Case 3
        input  = "nums = [1,1,2,2], n = 2"
        submit = func(obj, nums = [1,1,2,2], n = 2)
        answer = [1,2,1,2]
        self.check(input, submit, answer)

    @classmethod
    def _1675_minimize_deviation_in_array(self, obj, func) -> None:
        #   | Case 1
        input  = "nums = [1,2,3,4]"
        submit = func(obj, nums = [1,2,3,4])
        answer = 1
        self.check(input, submit, answer)

        #   | Case 2
        input  = "nums = [4,1,5,20,3]"
        submit = func(obj, nums = [4,1,5,20,3])
        answer = 3
        self.check(input, submit, answer)

        #   | Case 3
        input  = "nums = [2,10,8]"
        submit = func(obj, nums = [2,10,8])
        answer = 3
        self.check(input, submit, answer)