'''
Author  : Yuan-Yao Lou (Mike)
Title   : PhD student in ECE at Purdue University
Email   : yylou@purdue.edu
Website : https://yylou.github.io/
Date    : 2022/02/19
'''


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

        if ret: ret += f'\t(next: {cur.data})'
        return ret if ret else "'Empty'"

    # =============================================================

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

    # =============================================================

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

    # =============================================================

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

    # =============================================================

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
    
    # =============================================================

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

    # =============================================================

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

    # =============================================================

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


def josephus_circle(head: Node, step: int) -> Node:
    """
    Find the Winner of the Circular Game (Josephus Problem)
    """
    # Initialization (avoid affecting input linked list)
    l1 = LinkedList(head)
    print(f'\nOriginal List: {l1}')

    # (base case)
    n  = len(l1)
    if step == 1: return Node(n)

    prev, head = None, l1.head
    while n != 1:
        for _ in range(step - 1): prev, head = head, head.next
        if prev.next == l1.head: l1.head = prev.next.next
        
        print(f'Remove: {prev.next}')
        prev.next = prev.next.next
        head = prev.next
        n -= 1

    print(f'After (step={step}): {l1}')
    return Node(l1.head)


if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(1)                                                            # 1
    l1.append(2)                                                            # 2
    l1.append(3)                                                            # 3
    l1.append(4)                                                            # 4
    l1.append(5)                                                            # 12345
    
    l2 = LinkedList()
    l2.prepend(5)                                                           # 5
    l2.prepend(4)                                                           # 45
    l2.prepend(3)                                                           # 345
    l2.prepend(2)                                                           # 2345
    l2.prepend(1)                                                           # 12345

    l1 = LinkedList()
    l1.append(3)                                                            # 3
    l1.append(2)                                                            # 32
    l1.append(1)                                                            # 321
    print('\n[List 1]   ', l1)                                              # 321
    print('Remove 2:  ', LinkedList(l1.delete(2)))                          # 31
    print('Remove 1:  ', LinkedList(l1.delete(1)))                          # 3
    print('Remove 3:  ', LinkedList(l1.delete(3)))                          # 'Empty'

    l2.insert_after(l2.get_tail(), 6)                                       # 123456
    print('\n[List 2]   ', l2)                                              # 123456
    print('Length:    ', len(l2))                                           # 6
    print('Reverse:   ', LinkedList(l2.reverse_iterative()))                # 654321
    print('Reverse:   ', LinkedList(l2.reverse_recursive()))                # 123456
    print('Remove 6:  ', LinkedList(l2.delete(6)))                          # 12345
    print('Remove A:  ', LinkedList(l2.delete('A')))                        # 12345
    print('Rotate right 3: ', LinkedList(l2.rotate(3)))                     # 34512
    print('Rotate left  3: ', LinkedList(l2.rotate(3, dir='left')))         # 12345

    l2.insert_after(l2.get_node(2), 2)                                      # 122345
    l2.append(5)                                                            # 1223455        
    l3 = LinkedList(l2.append(5))                                           # 12234555
    print('\n[List 3]   ', l3)                                              # 12234555
    print('Remove Dup:   ', LinkedList(l3.removeDuplicates_ifSorted()))     # 12345
    
    l3.insert_after(l3.get_node(2), 2)                                      # 122345
    l3.append(5)                                                            # 1223455
    l4 = LinkedList(l3.append(5))                                           # 12234555
    print('\n[List 4]   ', l4)                                              # 12234555
    print('Remove Dup:   ', LinkedList(l4.removeDuplicates_set()))          # 12345

    l5 = LinkedList(l4.prepend('A'))                                        # A12345
    print('\n[List 5]    ', l5)                                             # A12345
    for i in range(1, len(l5)+1):
        print(f'[{i}-th last node]  {l5.get_nthToLast(i)}')                 # 5,4,3,2,1,A
    print(f'[Remove 6-th last node: {l5.get_nthToLast(6)}]')                # A
    print('[List 5]   ', LinkedList(l5.remove_nthToLast(6)))                # 12345
    print(f'[Remove 3-th last node: {l5.get_nthToLast(3)}]')                # 3
    print('[List 5]   ', LinkedList(l5.remove_nthToLast(3)))                # 1245
    print(f'[Remove 8-th last node: {l5.get_nthToLast(8)}]')                # 1
    print('[List 5]   ', LinkedList(l5.remove_nthToLast(8)))                # 245

    l4.insert_after(l4.get_node('A'), 'B')                                  # AB12345
    l4.insert_after(l4.get_node('B'), 'C')                                  # ABC12345
    l4.insert_after(l4.get_node('C'), 'D')                                  # ABCD12345
    l6 = LinkedList(l4.insert_after(l4.get_node('D'), 'E'))                 # ABCDE12345
    print('\n[List 6]    ', l6)                                             # ABCD12345
    print('Length:     ', len(l6))                                          # 10
    print(f'Middle Node: {l6.get_middle()}')                                # 1
    first, second = l6.split()
    print('1st Part:   ', LinkedList(first))                                # ABCDE
    print('2nd Part:   ', LinkedList(second))                               # 12345

    l7 = LinkedList(l6.merge(second))                                       # 12345ABCDE
    l7.remove_nthToLast(1)
    print('\n[List 7]    ', l7)                                             # 12345ABCD
    print('Length:     ', len(l7))                                          # 9
    print(f'Middle Node: {l7.get_middle()}')                                # 5
    first, second = l7.split()
    print('1st Part:   ', LinkedList(first))                                # 12345
    print('2nd Part:   ', LinkedList(second))                               # ABCD

    l6 = LinkedList(first)
    josephus_circle(l6.head, step=2)