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
        for function, object in self.__dict__.items():
            if function[1:5] == id: return object
        return None

    @classmethod
    def _0027_remove_element(self, nums: list[int], val: int) -> int:
        """  Easy  |  Two Pointer  """
        # Time:  O(n)
        # Space: O(1)

        l, r = 0, len(nums)-1
        while r >= 0 and nums[r] == val: r -= 1             # skip duplicate

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                while r >= 0 and nums[r] == val: r -= 1     # skip duplicate
            else:
                l += 1
        return l
    
    @classmethod
    def _0045_jump_game_II(self, nums: list[int]) -> int:
        def solution_1(nums) -> int:
            """  Medium  |  Greedy  """
            # Time:  O(n)
            # Space: O(1)

            jumps = 0
            left, right, maximum = 0, 0, 0
            while right < len(nums) - 1:    # before last element
                for idx in range(left, right+1):
                    maximum = max(maximum, idx + nums[idx])
                left = right + 1    # jump to next feasible range
                right = maximum
                jumps += 1

            return jumps
        
        def solution_2(nums) -> int:
            """  Medium  |  DP  """
            # Time:  O(n^2)
            # Space: O(n)

            n = len(nums)
            dp = [False for _ in range(n)]
            dp[-1] = True
            steps = [n for _ in range(n)]
            steps[-1] = 0
            for idx in range(n-2, -1, -1):
                for j in range(idx+1, min(n, idx+1+nums[idx])):
                    if dp[j] == True:   # find next stop with feasible path
                        dp[idx] = True
                        steps[idx] = min(steps[idx], steps[j] + 1)

            return steps[0] if dp[0] else False

        return solution_1(nums)

    @classmethod
    def _0055_jump_game(self, nums: list[int]) -> bool:
        def solution_1(nums) -> bool:
            """  Medium  |  DP  """
            # Time:  O(n)
            # Space: O(1)

            max_position = 0
            for idx in range(len(nums)):
                if idx > max_position: return False
                if max_position >= (len(nums) - 1): return True
                max_position = max(max_position, idx + nums[idx])

            return False
        
        def solution_2(nums) -> bool:
            """  Medium  |  DP  """
            # Time:  O(n^2)
            # Space: O(n)

            dp = [False for _ in range(len(nums))]
            dp[-1] = True
            for idx in range(len(nums)-2, -1, -1):
                for j in range(idx+1, min(len(nums), idx+1+nums[idx])):
                    if dp[j] == True:
                        dp[idx] = True
                        break

            return dp[0]

        return solution_1(nums)

    @classmethod
    def _0049_group_anagrams(self, strs: list[str]) -> list[list[str]]:
        """  Medium  |  Hash  """
        # Time:  O(mn)
        # Space: O(n)

        table = {}
        for string in strs:
            counter = [0 for _ in range(26)]
            for char in string: counter[ord(char) - ord("a")] += 1
            key = tuple(counter)
            table[key] = table.get(key, []) + [string]

        return table.values()

    @classmethod
    def _0088_merge_sorted_array(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """  Easy  |  Two Pointer  """
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
    def _0121_best_time_buy_sell_stock(self, prices: list[int]) -> int:
        """  Easy  |  DP  """
        # Time:  O(n)
        # Space: O(1)

        hold, sold = float("-inf"), 0
        for price in prices:
            preHold, preSold = hold, sold
            hold = max(preHold, 0 - price)  # preSold=0 as only allow one transaction
            sold = max(preSold, preHold + price)

        return sold
    
    @classmethod
    def _0122_best_time_buy_sell_stock_II(self, prices: list[int]) -> int:
        """  Medium  |  DP  """
        # Time:  O(n)
        # Space: O(1)

        hold, sold = float("-inf"), 0
        for price in prices:
            preHold, preSold = hold, sold
            hold = max(preHold, preSold - price)  # greedy
            sold = max(preSold, preHold + price)

        return sold

    @classmethod
    def _0217_contains_duplicate(self, nums: list[int]) -> bool:
        """  Easy  |  Hash  """
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

        def solution_1(nums: list[int], k: int) -> bool:
            """  Easy  |  Sliding Window + Hash  """
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
            """  Easy  |  Sliding Window + Hash  """
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
    def _0238_product_of_array_except_self(self, nums: list[int]) -> list[int]:
        """  Medium  |  Prefix Sum  """
        # Time:  O(n)
        # Space: O(1)

        output = [1 for _ in range(len(nums))]
        
        cur = 1
        for idx in range(len(nums)):    # 1, a1, a1a2, a1a2a3
            output[idx] *= cur
            cur *= nums[idx]

        cur = 1
        for idx in range(len(nums)-1, -1, -1):  # a2a3a4, a1a3a4, a1a2a4, a1a2a3
            output[idx] *= cur
            cur *= nums[idx]

        return output

    @classmethod
    def _0242_valid_anagram(self, s: str, t: str) -> bool:
        """  Easy  |  Hash  """
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
        """  Medium  |  Sliding Window + Hash  """
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
        """  Easy  |  Bit Operation  """
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
