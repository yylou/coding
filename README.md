# Coding Practice
> [Notion Pages](https://yylou.notion.site/CODING-eef2bf79104b44709c56f0bedea8d9f5)
> ![Notion](./notion.png)
> * #### Python Programming
>   * **Educative.io:** [```Python for Programmers```](https://www.educative.io/path/python-for-programmers) | [```Ace The Python Coding Interview```](https://www.educative.io/path/ace-python-coding-interview)
> * #### Problem Solving
>   * [```LeetCode```](https://leetcode.com/problemset/all/) | [```Bling 75```](https://www.techinterviewhandbook.org/best-practice-questions/) | [```NeetCode```](https://neetcode.io/roadmap)

<br />

## :soon: Interactive Mode
```python
>>> from Test import Test
>>> Test.run("0027", nums=[3,2,2,3], val=3)
[2, 2, 3, 3]
>>> Test.run("0088", nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
[1, 2, 2, 3, 5, 6]
```

```python
>>> from Array import Array
>>> import inspect
>>> code = inspect.getsource(Array.search("0027"))
>>> print(code)
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
```

## :on: Execution Mode
```python
> python3 main.py -prob 0242

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


    """

    [Input]     s = "anagram", t = "nagaram"
    [Answer]    True

    [Input]     s = "rat", t = "car"
    [Answer]    False

    """

```