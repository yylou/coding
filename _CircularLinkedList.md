# Python Coding

* ### [Menu](./README.md)
* ### Data Structures - Circular Linked List
    * [<ins>Source Code<ins>](./CircularLinkedList.py)
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
    * [Detect Cycle](#p11)
* ### LeetCode Problems
    * [0141. Linked List Cycle ```Easy```](https://leetcode.com/problems/linked-list-cycle/)
    * [0142. Linked List Cycle II ```Medium```](https://leetcode.com/problems/linked-list-cycle-ii/)
    * [1823. Find the Winner of the Circular Game ```Medium```](https://leetcode.com/problems/find-the-winner-of-the-circular-game/)

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

## Append / Prepend / Insert / Delete       <a name="p2"></a>
```python
    def append(self, data) -> Node:
        """
        Append a node to the end of the linked list
        - new node's next pointer = self.head
        """
        # (base case) no nodes in the linked list
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head

        else:
            tail = self.get_tail()
            tail.next = Node(data, self.head)

        return self.head

    def prepend(self, data) -> Node:
        """
        Append a node to the beginning of the linked list
        """
        # (base case) no nodes in the linked list
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head

        else:
            tail = self.get_tail()
            self.head = Node(data, self.head)
            tail.next = self.head

        return self.head

    def insert_after(self, node, data) -> Node:
        """
        Insert a node after a given node
        """
        # (base case)
        if not node: return

        new = Node(data)
        new.next = node.next
        node.next = new

        return self.head

    def delete(self, data) -> Node:
        """
        Search a node with specified data and remove from the linked list
        """
        # (base case)
        if not self.head: return

        # (1) Remove Head Node
        if self.head.data == data:
            # (a) Only one node in the list
            if self.head.next == self.head:
                self.head = None
                return

            # (b) More than one node in the list
            else:
                tail = self.get_tail()
                tail.next = self.head.next
                self.head = tail.next

        # (2) Remove Intermediate Node
        else:
            cur = self.head

            while cur:
                if cur.next.data == data:
                    cur.next = cur.next.next
                    break

                cur = cur.next
                if cur == self.head: break

        return self.head
```

## Merge                                    <a name="p3"></a>
```python
 def merge(self, node: Node) -> Node:
        """
        Merge with the other circular linked list while keeping sorted order
        """
        l1, l2 = self.head, node
        ret = cur = Node(-1)

        remain = (None, None)
        while True:
            if str(l1.data) < str(l2.data):
                cur.next = l1
                cur, l1 = cur.next, l1.next
                
                if l1 == self.head:
                    remain = (l2, node)
                    break
            else:
                cur.next = l2
                cur, l2 = cur.next, l2.next

                if l2 == node:
                    remain = (l1, self.head)
                    break

        # Concat the remaining part
        cur.next = remain[0]
        cur = cur.next
        while cur.next != remain[1]: cur = cur.next
        
        # Make it circular / Modify head node
        cur.next = ret.next
        self.head = ret.next
        
        return self.head
```

## Reverse                                  <a name="p4"></a>
```python
def reverse_iterative(self) -> Node:
        """
        Reverse the linked list iteratively
        - Take care of the tail node separately
        """
        # (base case) No nodes / Only one node
        if not self.head: return
        if self.head.next == self.head: return self.head

        # Intermediate Nodes (stop at tail node)
        prev, cur = None, self.head
        while cur.next != self.head:
            cur.next, prev, cur = prev, cur, cur.next

        # Tail Node
        cur.next = prev
        self.head.next = cur
        self.head = cur

        return self.head

    def reverse_recursive(self) -> Node:
        """
        Reverse the linked list recursively
        """
        # (base case) No nodes / Only one node
        if not self.head: return
        if self.head.next == self.head: return self.head

        def helper(cur):
            if not cur or cur.next == self.head: return cur

            # Keep recursion until the tail node is returned
            tail = helper(cur.next)

            cur.next.next = cur
            cur.next = None
            
            return tail
            
        tail = helper(self.head)
        
        # Make it circular / Assign head to returned tail node
        self.head.next = tail
        self.head = tail

        return self.head
```

## Rotate                                   <a name="p5"></a>
```python
    def rotate(self, n: int, dir: str='right') -> Node:
        """
        Rotate right or left
        ================================================================
        [Key] Only need to modify head node

        A -> B -> C -> D -> E (rotation = 2, length = 5)
        Right Rotate = D is new head node = 5 - 2 gapes from A
        Left  Rotate = C is new head node =     2 gapes from A
        ================================================================
        """
        length = self.__len__()

        # (base case) length == 1, n == length's multiple
        if length == 1: return self.head
        if n % length == 0: return self.head

        # Find new head node
        if   dir == 'right': rotation = length - n
        elif dir == 'left':  rotation = n
        for _ in range(rotation): self.head = self.head.next

        return self.head
```

## Get Middle Node                          <a name="p6"></a>
```python
def get_middle(self) -> Node:
        """
        Get the middle node of the linked list
        """
        # (base case) No node or only one node in the linked list
        if not self.head: return None
        if self.head.next == self.head: return self.head

        fastP, slowP = self.head, self.head

        # For even length, get the second middle node
        while fastP and fastP.next != self.head:
            fastP, slowP = fastP.next.next, slowP.next
            if fastP == self.head: break
            
        # For even length, get the first middle node
        '''
        while fastP and fastP.next != self.head and fastP.next.next != self.head:
            fastP, slowP = fastP.next.next, slowP.next
        '''
        
        return slowP
```

## Split                                    <a name="p7"></a>
```python
def split(self, n=2) -> tuple:
        """
        Split linked list into two parts
        - For even length, get the first middle node
        """
        # (base case) No node or only one node in the linked list
        if not self.head: return None, None
        if self.head.next == self.head: return self.head, None

        fastP, slowP = self.head, self.head

        # For even length, get the first middle node
        while fastP and fastP.next != self.head and fastP.next.next != self.head:
            fastP, slowP = fastP.next.next, slowP.next
            
        secondPart = slowP.next
        slowP.next, slowP = self.head, slowP.next
        
        # Make second part be circular
        while slowP.next != self.head: slowP = slowP.next
        slowP.next = secondPart

        return self.head, secondPart
```

# Remove n-th Last Node                     <a name="p8"></a>
```python
def remove_nthToLast(self, n: int) -> Node:
        """
        Remove the n-th node from the tail of the linked list
        """
        fastP, slowP = self.head, self.head

        # Find the node just before target node
        for _ in range(n): fastP = fastP.next
        while fastP.next != self.head: fastP, slowP = fastP.next, slowP.next

        slowP.next = slowP.next.next

        # If target node is the head node
        if fastP == slowP: self.head = slowP.next

        return self.head

    def get_nthToLast(self, n: int) -> Node:
        """
        Get the n-th node from the tail of the linked list
        """
        fastP, slowP = self.head, self.head

        # Find the node just before target node
        for _ in range(n): fastP = fastP.next
        while fastP.next != self.head: fastP, slowP = fastP.next, slowP.next

        return slowP.next
```

## Remove Duplicates                        <a name="p9"></a>
```python
def removeDuplicates_set(self) -> Node:
        # (Same method as the one for the singly linked list)
        """
        Remove nodes with duplicate data (using set)
        """
        record = set()
        prev, cur = None, self.head

        while cur:
            if cur.data in record:
                prev.next = cur.next
            else:
                record.add(cur.data)
                prev = cur
            
            cur = cur.next
            if cur == self.head: break

        return self.head

    def removeDuplicates_ifSorted(self) -> Node:
        # (Same method as the one for the singly linked list)
        """
        Remove nodes with duplicate data from sorted linked list
        """
        cur = self.head
        while cur:
            while cur.next and cur.data == cur.next.data:
                cur.next = cur.next.next

            cur = cur.next
            if cur == self.head: break
    
        return self.head
```

## Josephus Problem                         <a name="p10"></a>
```python
def josephus_circle(head: Node, step: int) -> Node:
    """
    Leetcode 1823. Find the Winner of the Circular Game (Medium) [https://leetcode.com/problems/find-the-winner-of-the-circular-game]
    - Find the Winner of the Circular Game (Josephus Problem)
    """
    # (base case)
    if step == 1: return head

    # Initialization (avoid affecting input linked list)
    l1 = LinkedList(head)
    print(f'\nOriginal List: {l1}')

    # (base case)
    n  = len(l1)
    if step == 1: return Node(n)

    prev, cur = None, l1.head
    while n != 1:
        print(f'Cur: {cur}, Prev: {prev}')
        
        for _ in range(step - 1): prev, cur = cur, cur.next
        if prev.next == l1.head: l1.head = prev.next.next
        
        print(f'Remove: {prev.next}', end='')
        prev.next = cur.next
        cur = prev.next
        print(f'\t({l1}')

        n -= 1

    print(f'After (step={step}): {l1}')
    return l1.head

    # Alternative Solution: Math
    """
    l1 = LinkedList(head)
    length = len(l1)

    index = 0
    for i in range(1, length+1): index = (index + step) % i
    winner = index + 1

    print(f'\nWinner of Josephus Problem: {winner}')

    cur = l1.head
    for _ in range(index): cur = cur.next
    return cur
    """
```

## Detect Cycle                             <a name="p11"></a>
```python
def linkedList_cycle(head: Node) -> tuple:
    """
    Leetcode 0141. Linked List Cycle    (Easy)   [https://leetcode.com/problems/linked-list-cycle/]
    Leetcode 0142. Linked List Cycle II (Medium) [https://leetcode.com/problems/linked-list-cycle-ii/]
    """
    # (base case) No nodes / Only one node
    if not head or not head.next: return False, None
    if head.next == head: return True, head
    
    slowP, fastP = head, head
    
    # 0141. Check whether the linked list has cycle or not
    while slowP and fastP and fastP.next:
        slowP, fastP = slowP.next, fastP.next.next
        if slowP == fastP: break

    # No cycle
    if slowP != fastP: return False, None
    
    # 0142. If there is cycle, find the entrance of the cycle
    slowP = head
    while slowP != fastP: slowP, fastP = slowP.next, fastP.next

    return True, slowP
```