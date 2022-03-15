# Python Coding

* ### [Menu](./README.md)                   <a name="p0"></a>
* ### Data Structures - Singly Linked List
    * [<ins>Source Code<ins>](./_SinglyLinkedList.py)
    * [Append / Prepend / Insert / Delete / Length](#p1)
    * [Swap Data / Swap Nodes / Swap Pairs](#p2)
    * [Reverse / Reverse Between](#p3)
    * [Rotate](#p4)
    * [Get Middle Node](#p5)
    * [Split / Split in Parts](#p6)
    * [Sort](#p7)
    * [Remove n-th Last Node](#p8)
    * [Remove Duplicates](#p9)
    * [Merge Two Sorted Linked Lists](#p10)
    * [Reorder](#p11)
* ### LeetCode Problems
    * [0002. Add Two Numbers ```Medium```](https://leetcode.com/problems/add-two-numbers/)
    * [0019. Remove Nth Node From End of List ```Medium```](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
    * [0021. Merge Two Sorted Lists ```Easy```](https://leetcode.com/problems/merge-two-sorted-lists/)
    * [0023. Merge k Sorted Lists ```Hard```](https://leetcode.com/problems/merge-k-sorted-lists/)
    * [0024. Swap Nodes in Pairs ```Medium```](https://leetcode.com/problems/swap-nodes-in-pairs/)
    * [0025. Reverse Nodes in k-Group ```Hard```](https://leetcode.com/problems/reverse-nodes-in-k-group/)
    * [0061. Rotate List ```Medium```](https://leetcode.com/problems/rotate-list/)
    * [0083. Remove Duplicates from Sorted List ```Easy```](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
    * [0092. Reverse Linked List II ```Medium```](https://leetcode.com/problems/reverse-linked-list-ii/)
    * [0138. Copy List with Random Pointer ``Medium```](https://leetcode.com/problems/copy-list-with-random-pointer/)
    * [0141. Linked List Cycle ```Easy```](https://leetcode.com/problems/linked-list-cycle/)
    * [0142. Linked List Cycle II ```Medium```](https://leetcode.com/problems/linked-list-cycle-ii/)
    * [0143. Reorder List ```Medium```](https://leetcode.com/problems/reorder-list/)
    * [0148. Sort List ```Medium```](https://leetcode.com/problems/sort-list/)
    * [0160. Intersection of Two Linked Lists ```Easy```](https://leetcode.com/problems/intersection-of-two-linked-lists/)
    * [0203. Remove Linked List Elements ```Easy```](https://leetcode.com/problems/remove-linked-list-elements/)
    * [0206. Reverse Linked List ```Easy```](https://leetcode.com/problems/reverse-linked-list/)
    * [0234. Palindrome Linked List ```Easy```](https://leetcode.com/problems/palindrome-linked-list/)
    * [0237. Delete Node in a Linked List ```Easy```](https://leetcode.com/problems/delete-node-in-a-linked-list/)
    * [0328. Odd Even Linked List ```Medium```](https://leetcode.com/problems/odd-even-linked-list/)
    * [0445. Add Two Numbers II ```Medium```](https://leetcode.com/problems/add-two-numbers-ii/)
    * [0725. Split Linked List in Parts ```Medium```](https://leetcode.com/problems/split-linked-list-in-parts/)
    * [0876. Middle of the Linked List ```Easy```](https://leetcode.com/problems/middle-of-the-linked-list/)
    * [1721. Swapping Nodes in a Linked List ```Mdeium```](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)
    * [2095. Delete the Middle Node of a Linked List ```Medium```](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)
    * [2130. Maximum Twin Sum of a Linked List ```Medium```](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)

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
            while head:
                self.append(head.data)
                head = head.next

    def __str__(self) -> str:
        """
        Print the linked list from HEAD to the TAIL node
        """
        ret = ''

        cur = self.head
        while cur:
            ret += str(cur.data)
            cur = cur.next
        
        return ret

    def get_node(self, key) -> Node:
        """
        Retrieve node by key (data)
        """
        cur = self.head
        while cur: 
            if cur.data == key: return cur
            cur = cur.next

        return None

    def get_tail(self) -> Node:
        """
        Retrieve the tail node
        """
        cur = self.head
        while cur.next: cur = cur.next
        
        return cur
```

## Append                                   <a name="p1"></a>
```python
    def append(self, data) -> Node:
        """
        Add new node to the end of the linked list
        """
        new = Node(data)

        # (base case) no nodes
        if not self.head: self.head = new

        else: 
            cur = self.head
            while cur.next: cur = cur.next
            cur.next = new

        return self.head
```

## Prepend
```python
    def prepend(self, data) -> Node:
        """
        Add new node to the head of the linked list
        """
        new = Node(data, self.head)
        self.head = new

        return self.head
```

## Insert
```python
    def insert_after(self, node, data) -> Node:
        """
        Add new node after the specific node
        """
        new = Node(data)
        new.next = node.next
        node.next = new

        return self.head
```

## Delete
```python
    def delete(self, key) -> Node:
        """
        Delete node by searching key as node's data
        """
        cur = self.head

        # Node to be deleted is head
        if cur.data == key:
            self.head = cur.next
            cur = None

        # Search for the node before the node to be deleted
        else:
            while cur.next and cur.next.data != key: cur = cur.next
            if cur.next: cur.next = cur.next.next

        return self.head

    def delete_pos(self, pos) -> Node:
        """
        Delete node by its position
        """
        # Node to be deleted is head
        if pos == 0 and self.head:
            self.head = self.head.next
        
        else:
            cur, prev, index = self.head, None, 1
            while cur and index != pos:
                cur, prev, index = cur.next, cur, index+1
            if cur: prev.next, cur = cur.next, None

        return self.head
```

## Length
```python
    def __len__(self) -> int:
        """
        Get the length of the linked list (iterative)
        """
        cur, count = self.head, 0
        while cur: cur, count = cur.next, count+1
        return count

    def get_len_recursive(self, node) -> int:
        """
        Get the length of the linked list (recursive)
        """
        if not node: return 0
        return 1 + self.get_len_recursive(node.next)
```

### Swap Data / Swap Nodes / Swap Pairs     <a name="p2"></a>
```python
    def swap_data(self, key1, key2) -> Node:
        """
        Swap two nodes' data by searching key (node's data)
        """
        # Iterate the list to find two target nodes
        cur, node1, node2 = self.head, None, None
        while cur:
            if cur.data == key1: node1 = cur
            if cur.data == key2: node2 = cur
            cur = cur.next

        if node1 and node2: node1.data, node2.data = node2.data, node1.data

        return self.head

    def swap_node(self, key1, key2) -> Node:
        """
        Swap two nodes by searching key (node's data)
        """
        cur, prev = self.head, None
        prev1, node1, prev2, node2 = None, None, None, None

        # Iterate the list to find two target nodes and their previous nodes
        while cur:
            if   cur.data == key1: node1, prev1 = cur, prev
            elif cur.data == key2: node2, prev2 = cur, prev
            
            cur, prev = cur.next, cur

        # Return: Both nodes not exist | Two nodes are the same
        if not (node1 and node2) or (node1 == node2): return

        # Node1's previous node exists, assign next pointer to node2
        if prev1: prev1.next = node2
        # Otherwise, assign node2 to head node
        else: self.head = node2

        # Node1's previous node exists, assign next pointer to node2
        if prev2: prev2.next = node1
        # Otherwise, assign node2 to head node
        else: self.head = node1

        # Swap node1 and node2's next pointers
        node1.next, node2.next = node2.next, node1.next

        return self.head

    def swap_nodes(self, k: int) -> Node:
        """
        Leetcode 1721. Swapping Nodes in a Linked List (Medium) [(https://leetcode.com/problems/swapping-nodes-in-a-linked-list/]
        - Swap the kth node from the beginning and the kth node from the end
        """
        ret = prev1 = prev2 = Node(0, self.head)
        cur = self.head
        
        # Find the previous nodes
        for _ in range(k - 1): prev1, cur = cur, cur.next
        while cur and cur.next: prev2, cur = prev2.next, cur.next
            
        # If node to be swapped is the middle one
        if prev1.next == prev2.next: return self.head
        
        # Swap nodes
        node1, node2 = prev1.next, prev2.next
        prev1.next, prev2.next = node2, node1
        node1.next, node2.next = node2.next, node1.next
        
        self.head = ret.next
        return self.head

    def swap_pairs(self) -> Node:
        """
        Leetcode 0024. Swap Nodes in Pairs (Medium) [https://leetcode.com/problems/swap-nodes-in-pairs/]
        """
        # (base case)
        if not self.head: return None
        if not self.head.next: return self.head

        ret = prev = Node(0, self.head)
        cur = self.head

        while cur and cur.next:
            tmp = cur.next.next
            cur.next.next = cur
            prev.next = cur.next
            cur.next = tmp

            cur, prev = tmp, cur

        self.head = ret.next
        return self.head
```

## Reverse / Reverse Between                <a name="p3"></a>
```python
    def reverse_iterative(self) -> Node:
        """
        Reverse the linked list by iterative method
        """
        cur, prev = self.head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev

        return self.head

    def reverse_recursive(self) -> Node:
        """
        Reverse the linked list by recursive method
        """
        def helper(cur):
            # No node in the list / Only 1 node in the list
            if not cur or not cur.next: return cur
            
            # Keep recursion until the tail node, which is returned
            tail = helper(cur.next)

            '''
                    (cur)  (tail)
            A -> B -> C -> D    None
                        <-

                    (cur)  (tail)
            A -> B -> C <- D    None
                      |-> None

               (cur)       (tail)
            A -> B -> C <- D    None
                   <-

               (cur)       (tail)
            A -> B <- C <- D    None
                 |-> None

            (cur)            (tail)
            A -> B -> C <- D    None
              <-

            (cur)            (tail=HEAD)
            A <- B <- C <- D    None
            |-> None
            '''
            cur.next.next = cur
            cur.next = None

            return tail
        
        tail = helper(self.head)
        self.head = tail

        return self.head

    def reverse_between(self, left: int, right: int) -> Node:
        """
        Leetcode 0092. Reverse Linked List II (Medium) [https://leetcode.com/problems/reverse-linked-list-ii/]
        """ 
        # (base case)
        if left == right: return self.head

        ret = cur = Node(0, self.head)
        
        for _ in range(left - 1): cur = cur.next
        start = cur

        prev, cur = cur, cur.next
        for _ in range(right - left + 1):
            cur.next, cur, prev = prev, cur.next, cur

        start.next.next = cur
        start.next = prev

        self.head = ret.next
        return ret.next
```

## Rotate                                   <a name="p4"></a>
```python
    def rotate(self, n: int, dir: str='right') -> Node:
        """
        Rotate right or left
        ================================================================
        [Key] Find Original Tail Node & New Tail Node

        A -> B -> C -> D -> E (rotation = 2, length = 5)
        Right Rotate = C is new tail node = 5 - 2 - 1 gaps from A
                       D is new head node

        Left  Rotate = B is new tail node = 2 - 1     gaps from A
                       C is new head node
        ================================================================
        """
        # (base case) No node / Only one node
        if not self.head or not self.head.next: return self.head

        # Find tail node
        tail, length = self.head, 1
        while tail.next: tail, length = tail.next, length + 1

        n %= length
        if n == 0: return self.head

        if   dir == 'right': rotation = length - n - 1
        elif dir == 'left':  rotation = n - 1

        # Find new tail node
        new_tail = self.head    
        for _ in range(rotation): new_tail = new_tail.next

        new_head, new_tail.next = new_tail.next, None
        tail.next = self.head
        self.head = new_head

        return self.head
```

## Get Middle Node                          <a name="p5"></a>
```python
    def get_middle(self) -> Node:
        """
        Get the middle node of the linked list
        """
        # (base case) No node or only one node in the linked list
        if not self.head: return None
        if not self.head.next: return self.head
        
        fastP, slowP = self.head, self.head

        # For even length, get the second middle node
        while fastP and fastP.next: 
            fastP, slowP = fastP.next.next, slowP.next

        # For even length, get the first middle node
        '''
        while fastP and fastP.next and fastP.next.next: 
            fastP, slowP = fastP.next.next, slowP.next
        '''
            
        return slowP
```

## Split / Split in Parts                   <a name="p6"></a>
```python
    def split(self) -> tuple:
        """
        Split linked list into two parts
        - For even length, get the first middle node
        """
        # (base case) No node or only one node in the linked list
        if not self.head: return None, None
        if not self.head.next: return self.head, None

        fastP, slowP = self.head, self.head

        # For even length, get the first middle node
        while fastP and fastP.next and fastP.next.next: 
            fastP, slowP = fastP.next.next, slowP.next

        secondPart, slowP.next = slowP.next, None
        
        return self.head, secondPart

    def split_inParts(self, step: int) -> list:
        """
        Split linked list into several parts 
        """
        # (base case) No nodes / Only one node
        if not self.head: return [None for _ in range(step)]
        if not self.head.next: return [self.head] + [None for _ in range(step - 1)]

        width, remain = divmod(self.__len__(), step)
        
        ret = []
        cur = Node(None, self.head)
        for i in range(step):
            start = cur
            for _ in range(width + (i < remain)): cur = cur.next
            ret.append(start.next)
            start.next = None

        return ret
```

## Sort                                     <a name="p7"></a>
```python
    def sort(self) -> Node:
        """
        Leetcode 0148. Sort List (Medium) [https://leetcode.com/problems/sort-list/]
        - Sort the linked list (using bottom-up Merge Sort)
        """ 
        # (base case)
        if not self.head or not self.head.next: return self.head

        length = self.__len__()
        ret, size = Node(0, self.head), 1

        while size < length:
            splitHead, mergeHead = ret.next, ret

            while splitHead:
                left      = splitHead
                right     = self._split(size, left)
                splitHead = self._split(size, right)

                mergeHead = self._merge(left, right, mergeHead)

            size *= 2

        self.head = ret.next
        return self.head

    def _split(self, size: int, node: Node) -> Node:
        prev, cur = None, node
        for _ in range(size):
            if not cur: break
            prev, cur = cur, cur.next
        
        if prev: prev.next = None
        return cur

    def _merge(self, left: Node, right: Node, head: Node) -> Node:
        while left and right:
            if str(left.data) <= str(right.data): head.next, left = left, left.next
            else: head.next, right = right, right.next

            head = head.next

        head.next = left or right
        while head.next: head = head.next
        return head
```

## Remove n-th Last Node                    <a name="p8"></a>
```python
    def remove_nthToLast(self, n: int) -> Node:
        """
        Remove the n-th node from the tail of the linked list
        """
        fastP, slowP = self.head, self.head

        '''
        n = 3
        (slowP)          (fastP)
        1 -> 2 -> '3' -> 4 -> 5
        '''
        for _ in range(n):
            try:
                fastP = fastP.next
            except:
                print('[Error] n > length of linked list')
                return self.head

        if not fastP: 
            self.head = self.head.next
            return self.head

        '''
        n = 3
             (slowP)          (fastP)
        1 -> 2 -> '3' -> 4 -> 5
        '''
        while fastP.next: fastP, slowP = fastP.next, slowP.next

        slowP.next = slowP.next.next
        return self.head

    def get_nthToLast(self, n: int) -> Node:
        """
        Get the n-th node from the tail of the linked list
        """
        fastP, slowP = self.head, self.head

        for _ in range(n):
            try:
                fastP = fastP.next
            except:
                print('[Error] n > length of linked list')
                return self.head

        # n == legnth
        if not fastP: return self.head

        # Find the node just before target node
        while fastP.next: fastP, slowP = fastP.next, slowP.next
        
        return slowP.next
```

## Remove Duplicates                        <a name="p9"></a>
```python
    def removeDuplicate_set(self) -> Node:
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

        return self.head

    def removeDuplicate_ifSorted(self) -> Node:
        """
        Remove nodes with duplicate data from sorted linked list
        """
        cur = self.head
        while cur:
            while cur.next and cur.data == cur.next.data:
                cur.next = cur.next.next

            cur = cur.next

        return self.head
```

## Merge Two Sorted Linked Lists            <a name="p10"></a>
```python
def mergeTwoLists_iterative(l1, l2) -> Node:
    """
    Merge two linked lists by iterative method
    """
    ret = cur = Node(0)

    while l1 and l2:
        if l1.data < l2.data:
            cur.next = l1
            cur, l1 = cur.next, l1.next
        else:
            cur.next = l2
            cur, l2 = cur.next, l2.next
    
    cur.next = l1 or l2
    return ret.next

def mergeTwoLists_recursive(l1, l2) -> Node:
    """
    Merge two linked lists by recursive method
    """
    if not l1: return l2
    if not l2: return l1

    if l1.data > l2.data: l1, l2 = l2, l1
    l1.next = mergeTwoLists_recursive(l1.next, l2)

    return l1
```

### Reorder                                 <a name="p11"></a>
```python
def reorder(head: Node) -> None:
    """
    Leetcode 0143. Reorder List (Medium) [https://leetcode.com/problems/reorder-list/]
    """
    # (base case) No node / Only one node / Two nodes
    if not head: return None
    if not head.next: return head
    if not head.next.next: return head

    # 1. Find middle point
    slowP, fastP = head, head
    while fastP and fastP.next and fastP.next.next:
        slowP, fastP = slowP.next, fastP.next.next
    
    # 2. Reverse second part
    prev, slowP.next, slowP = None, None, slowP.next
    while slowP: prev, slowP.next, slowP = slowP, prev, slowP.next

    # 3. Merge
    while prev:
        head.next, head = prev, head.next
        prev.next, prev = head, prev.next
```