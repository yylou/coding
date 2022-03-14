# Python Coding

* ### [Menu](./README.md)
* ### Data Structures - Circular Linked List
    * [<ins>Source Code<ins>](./_CircularLinkedList.py)
    * [\_\_len\_\_ / \_\_str\_\_](#p1)
    * [Append / Prepend / Insert / Delete](#p2)
    * [Merge](#p3)
    * [Reverse](#p4)
    * [Rotate](#p5)
    * [Get Middle Node](#p6)
    * [Split](#p7)
    * [Remove n-th Last Node](#p8)
    * [Remove Duplicates](#p9)
    * [Josephus Problem](#p10)
* ### LeetCode Problems
    * [0141. Linked List Cycle (Easy)](https://leetcode.com/problems/linked-list-cycle/)
    * [0142. Linked List Cycle II (Medium)](https://leetcode.com/problems/linked-list-cycle-ii/)
    * [1823. Find the Winner of the Circular Game (Medium)](https://leetcode.com/problems/find-the-winner-of-the-circular-game/)

<br />

## Linked List
```python
# For Python3 Compatibility
from __future__ import print_function


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = None

        if head: 
            cur = head
            while cur:
                self.append(cur.data)
                cur = cur.next
                if cur == head: break

    def get_node(self, key) -> Node:
        """
        Retrieve node by key (data)
        """
        cur = self.head
        while cur: 
            if cur.data == key: return cur
            cur = cur.next
            if cur == self.head: break

        return None

    def get_tail(self) -> Node:
        """
        Retrieve the tail node
        """
        # (base case)
        if not self.head: return None
        if self.head.next == self.head: return self.head

        cur = self.head
        while cur.next != self.head: cur = cur.next

        return cur
```

## \_\_len\_\_ / \_\_str\_\_                <a name="p1"></a>
```python
    def __len__(self) -> int:
        """
        Return the length of the linked list
        """
        # (base case)
        if not self.head: return 0
        if self.head.next == self.head: return 1

        cur = self.head
        length = 0
        while cur:
            length += 1
            cur = cur.next
            if cur == self.head: break

        return length

    def __str__(self) -> str:
        """
        Print the linked list from HEAD to the TAIL node
        """
        # (base case)
        if not self.head: return "'Empty'"
        if self.head.next == self.head: return str(self.head.data) + f'\t(next: {self.head.data})'

        ret = ''

        cur = self.head
        while cur:
            ret += str(cur.data)
            cur = cur.next
            if cur == self.head: break

        if ret and cur: ret += f'\t(next: {cur.data})'
        return ret if ret else "'Empty'"
```

