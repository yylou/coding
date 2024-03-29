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
    def _0001_two_sum(self, nums: list[int], target: int) -> list[int]:
        """  Easy  |  Hash  """
        # Time:  O(n)
        # Space: O(n)

        table = {}
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in table: return [table[remain], idx]
            else: table[num] = idx

    @classmethod
    def _0011_container_with_most_water(self, height: list[int]) -> int:
        """  Medium  |  Two Pointer  """
        # Time:  O(n)
        # Space: O(1)

        area = 0
        l, r = 0, len(height)-1
        while l < r:
            gap  = r - l
            area = max(area, gap * min(height[l], height[r]))
            if height[l] < height[r]: l += 1
            else: r -= 1
            
        return area    

    @classmethod
    def _0015_3sum(self, nums: list[int]) -> list[list[int]]:
        """  Medium  |  Hash  """
        # Time:  O(n)
        # Space: O(n)

        ans = set()
        neg, zero, pos = {}, {}, {}
        for num in nums:
            if   num  < 0: neg[num]  = neg.get(num, 0) + 1
            elif num == 0: zero[num] = zero.get(num, 0) + 1
            elif num  > 0: pos[num]  = pos.get(num, 0) + 1

        if zero:
            if zero[0] > 2: ans.add((0, 0, 0))
            for num in pos:
                if -num in neg:
                    ans.add((-num, 0, num))

        if pos:
            for n1, counter in neg.items():
                for n2, counter in neg.items():
                    remain = -(n1 + n2)
                    if remain in pos:
                        if n1 == n2 and counter > 1: ans.add((min(n1, n2), max(n1, n2), remain))
                        elif n1 != n2: ans.add((min(n1, n2), max(n1, n2), remain))

        if neg:
            for n1, counter in pos.items():
                for n2, counter in pos.items():
                    remain = -(n1 + n2)
                    if remain in neg:
                        if n1 == n2 and counter > 1: ans.add((remain, min(n1, n2), max(n1, n2)))
                        elif n1 != n2: ans.add((remain, min(n1, n2), max(n1, n2)))

        return ans

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
    def _0036_valid_sudoku(self, board: list[list[str]]) -> bool:
        """  Medium  |  Bit Operation  """
        # Time:  O(n^2)
        # Space: O(n)

        row, col, block = [0]*9, [0]*9, [0]*9
        for rid in range(9):
            for cid in range(9):
                if board[rid][cid] == ".": continue

                num = int(board[rid][cid])
                bid = rid//3 * 3 + cid//3
                if ((row[rid] >> num) & 1) or ((col[cid] >> num) & 1) or ((block[bid] >> num) & 1):
                    return False
                else:
                    row[rid] |= (1 << num)
                    col[cid] |= (1 << num)
                    block[bid] |= (1 << num)
        return True

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

        return solution_1(nums=nums)
        return solution_2(nums=nums)

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
    def _0053_maximum_subarray(self, nums: list[int]) -> int:
        def solution_1(nums):
            """  Medium  |  DP  """
            # Time:  O(n)
            # Space: O(n)

            stack, dp = [], []              # (optional)
            local, ans = float("-inf"), float("-inf")
        
            for num in nums:
                if local + num > num:
                    stack.append(num)
                    local += num
                else:
                    stack = [num]
                    local = num

                dp.append((local, stack))   # (optional)
                ans = max(ans, local)

            return ans
        
        def solution_2(nums: list, l: int, r: int):
            """  Medium  |  Divide and Conquer  """
            # Time:  O(n)
            # Space: O(1)
            
            if l > r: return float("-inf")
            mid = (l + r) // 2

            # LEFT | RIGHT
            l_max = solution_2(nums, l, mid-1)
            r_max = solution_2(nums, mid+1, r)

            # MIDDLE
            tmp = l_part = 0
            for i in range(mid-1, l-1, -1):
                tmp += nums[i]
                l_part = max(l_part, tmp)
            tmp = r_part = 0
            for i in range(mid+1, r+1, 1):
                tmp += nums[i]
                r_part = max(r_part, tmp)

            return max(l_max, r_max, l_part + nums[mid] + r_part)

        return solution_1(nums=nums)
        return solution_2(nums=nums, l=0, r=len(nums)-1)

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

        return solution_1(nums=nums)
        return solution_2(nums=nums)

    @classmethod
    def _0056_merge_intervals(self, intervals: list[list[int]]) -> list[list[int]]:
        """  Medium  |  Sorting  """
        # Time:  O(nlogn + n)
        # Space: O(1)

        intervals.sort(key=lambda x: x[0])

        ans = []
        for interval in intervals:
            #   (initial)
            if not ans: ans.append(interval)

            #   (out of range)
            elif not (ans[-1][0] <= interval[0] <= ans[-1][1]): ans.append(interval)

            #   (overlap: merge and update)
            else:
                ans[-1][0] = min(ans[-1][0], interval[0])
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans

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
            hold = max(preHold, 0 - price)  # preSold=0 as only allow 1 transaction
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
    def _0152_maximum_product_subarray(self, nums: list[int]) -> int:
        """  Medium  |  DP  """
        # Time:  O(n)
        # Space: O(1)

        ans = float("-inf")
        local_min, local_max = 1, 1
        for num in nums:
            #   (use tmp variable or write in one-liners)
            _min = min(local_min*num, num, local_min*num)
            _max = max(local_max*num, num, local_max*num)
            local_min, local_max = _min, _max
            
            ans = max(ans, local_max)
        return ans

    @classmethod
    def _0167_two_sum_II_input_array_sorted(self, numbers: list[int], target: int) -> list[int]:
        def solution_1(numbers, target):
            """  Medium  |  Two Pointer  """
            # Time:  O(n)
            # Space: O(1)

            l, r = 0, len(numbers)-1
            while l < r:
                total = numbers[l] + numbers[r]
                if total == target: return [l+1, r+1]
                if total > target: r -= 1
                else: l += 1

        def solution_2(numbers, target):
            """  Medium  |  Binary Search  """
            # Time:  O(nlogn)
            # Space: O(1)

            for idx, val in enumerate(numbers):
                remain = target - val
                l, r = idx+1, len(numbers)
                while l < r:
                    mid = (l + r) // 2
                    if numbers[mid] == remain: return [idx+1, mid+1]
                    if numbers[mid] > remain: r = mid
                    else: l = mid + 1

        return solution_1(numbers=numbers, target=target)
        return solution_1(numbers=numbers, target=target)

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
        def solution_1(nums) -> list[int]:
            """  Medium  |  Prefix Sum  """
            # Time:  O(n)
            # Space: O(1)

            output = [1 for _ in range(len(nums))]
            prefix = 1
            suffix = 1

            for idx in range(len(nums)):
                #   | Prefix product:      1,   a1, a1a2, a1a2a3
                output[idx] *= prefix
                prefix *= nums[idx]
                #   | Suffix product: a2a3a4, a3a4,   a4,      1
                output[-1-idx] *= suffix
                suffix *= nums[-1-idx]
                
            return output

        def solution_2(nums) -> list[int]:
            """  Medium  |  Prefix Sum  """
            # Time:  O(n)
            # Space: O(1)

            output = [1 for _ in range(len(nums))]
            
            cur = 1
            for idx in range(len(nums)):  # 1, a1, a1a2, a1a2a3
                output[idx] *= cur
                cur *= nums[idx]

            cur = 1
            for idx in range(len(nums)-1, -1, -1):  # a2a3a4, a3a4, a4, 1
                output[idx] *= cur
                cur *= nums[idx]

            return output
        
        return solution_1(nums=nums)
        return solution_2(nums=nums)

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
    def _0347_top_k_frequent_elements(self, nums: list[int], k: int) -> list[int]:
        def solution_1(nums: list[int], k: int) -> list[int]:
            """  Medium  |  QuickSelect  """
            # Time:  O(n)
            # Space: O(n)

            from collections import Counter
            freq = Counter(nums)
            freq_keys = list(freq.keys())
            n = len(freq_keys)

            def partition(l, r):
                pivot = freq_keys[r]
                place = l
                for i in range(place, r):
                    if freq[freq_keys[i]] < freq[pivot]: 
                        freq_keys[i], freq_keys[place] = freq_keys[place], freq_keys[i]
                        place += 1
                freq_keys[place], freq_keys[r] = freq_keys[r], freq_keys[place]
                return place

            def quick_select(l: int, r: int, k: int):
                idx = partition(l, r)
                if   idx == k: return
                elif idx  > k: quick_select(l, idx-1, k)
                elif idx  < k: quick_select(idx+1, r, k)

            quick_select(l=0, r=n-1, k=n-k)
            return freq_keys[n-k:]

        def solution_2(nums: list[int], k: int) -> list[int]:
            """  Medium  |  Heap  """
            # Time:  O(n + klogn)
            # Space: O(n)

            import heapq
            from collections import Counter
            counter = Counter(nums)
            heap = [(-freq, num) for num, freq in counter.items()]  # maxHeap = -freq
            heapq.heapify(heap)
            
            ans = []
            while len(ans) < k:
                freq, num = heapq.heappop(heap)
                ans.append(num)
            return ans

        def solution_3(nums: list[int], k: int) -> list[int]:
            """  Medium  |  Bucket Sort  """
            # Time:  O(n)
            # Space: O(10^5)

            from collections import Counter
            counter = Counter(nums)
            bucket = [[] for _ in range(len(nums) + 1)]     # Frequency is 0-indexed = length + 1
            for num, freq in counter.items(): bucket[freq].append(num)
            
            freq = len(nums)
            ans = []
            while len(ans) < k:
                while bucket[freq] == []: freq -= 1
                for num in bucket[freq]: 
                    ans.append(num)
                    if len(ans) >= k: return ans
                freq -= 1
            return ans
        
        def solution_4(nums: list[int], k: int) -> list[int]:
            """  Medium  |  Hash + Sort  """
            # Time:  O(n + nlogn)
            # Space: O(n)

            from collections import Counter
            counter = Counter(nums)
            ans = []
            return sorted(counter, key=lambda x: counter[x], reverse=True)[:k]

        return solution_1(nums=nums, k=k)       
        return solution_2(nums=nums, k=k)
        return solution_3(nums=nums, k=k)
        return solution_4(nums=nums, k=k)

    @classmethod
    def _0502_IPO(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        """  Medium  |  Greedy, Sort, Heap  """

        import heapq
        candidate = []

        idx = 0
        projects = sorted(zip(capital, profits))
        for _ in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                heapq.heappush(candidate, -projects[idx][1])
                idx += 1
            if not candidate: break
            w += -heapq.heappop(candidate)

        return w

    @classmethod
    def _0904_fruit_into_baskets(self, fruits: list[int]) -> int:
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
    def _1011_capacity_to_ship_packages_within_d_days(self, weights: list[int], days: int) -> int:
        """  Medium  |  Binary Search  """
        # Time:  O(n * logn)
        # space: O(1)

        def validate(weights, capacity, days):
            cur = 0
            for package in weights:
                cur += package
                if cur > capacity:
                    days -= 1
                    cur = package   # (reload)
            return days > 0

        #   | Search space: [min, max]
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            if validate(weights, capacity=mid, days=days):  # (feasible)
                r = mid
            else:
                l = mid + 1
        
        return l

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
