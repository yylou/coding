'''
Author  : Yuan-Yao Lou (Mike)
Title   : PhD student in ECE at Purdue University
Email   : yylou@purdue.edu
Website : https://yylou.github.io/
Date    : 2022/03/15
'''


# For Python3 Compatibility
from __future__ import print_function


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self, head: Node=None):
        self.head = None

        if head:
            while head:
                self.append(head.data)
                head = head.next

    # =============================================================

    def __len__(self) -> int:
        """
        Get the length of the linked list (iterative)
        """
        cur, n = self.head, 0
        while cur: cur, n = cur.next, n+1
        
        return n

    def getLen_Iterative(self) -> int:
        """
        Get the length of the linked list (iterative)
        """
        return self.__len__()

    def getLen_Recursive(self, node: Node) -> int:
        """
        Get the length of the linked list (recursive)
        """
        # (base case)
        if not node: return 0
        return 1 + self.getLen_Recursive(node.next)

    def __str__(self) -> str:
        """
        Print the doubly linked list
        """
        ret = ''

        cur = self.head
        while cur: ret, cur = f'{ret}{cur.data}', cur.next

        return ret

    def summary(self) -> None:
        """
        Print the detailed information of the linked list
        """
        print('==================================================')
        print(f'List: {self}')
        cur = self.head
        while cur:
            print(f'Node: {cur}    (Previous Node: {cur.prev if cur.prev else "-"}, Next Node: {cur.next if cur.next else "-"})')
            cur = cur.next
        print('==================================================')

    # =============================================================

    def getTail(self) -> Node:
        """
        Get the tail node
        """
        cur = self.head
        while cur.next: cur = cur.next

        return cur

    def append(self, data: str) -> Node:
        """
        Append node to the linked list (insert after tail)
        """
        # (1) No nodes
        if not self.head:
            self.head = Node(data)
        
        # (2) Have nodes
        else:
            tail = self.getTail()
            tail.next = Node(data, prev=tail, next=None)
        
        return self.head

    def prepend(self, data: str) -> Node:
        """
        Prepend node to the linked list (insert before head)
        """
        # (1) No nodes
        if not self.head:
            self.head = Node(data)
        
        # (2) Have nodes
        else:
            self.head = Node(data, prev=None, next=self.head)
            self.head.next.prev = self.head
        
        return self.head

    def insertBefore(self, data: str, key: str) -> Node:
        """
        Insert node before the node that has key data
        """
        target = self.head
        while target and target.data != key: target = target.next

        if target:
            target.prev.next = Node(data, prev=target.prev, next=target)
            target.prev = target.prev.next
        
        return self.head

    def insertAfter(self, data: str, key: str) -> Node:
        """
        Insert node after the node that has key data
        """
        target = self.head
        while target and target.data != key: target = target.next

        if target:
            target.next.prev = Node(data, prev=target, next=target.next)
            target.next = target.next.prev
        
        return self.head

    def delete(self, key: str) -> Node:
        """
        Delete node from the linked list
        """
        target = self.head
        while target and target.data != key: target = target.next

        if target:
            # (1) Head node
            if not target.prev:
                self.head = self.head.next
                self.head.prev = None

            # (2) Tail node
            elif not target.next:
                target.prev.next = None

            # (3) Intermediate node
            else:
                target.prev.next = target.next
                target.next.prev = target.prev
        
        return self.head

    # =============================================================

    def reverse(self) -> Node:
        """
        Reverse the linked list
        """
        # (base case)
        if not self.head or not self.head.next: return

        prev, cur = None, self.head
        while cur:
            prev = cur
            cur.next, cur.prev, cur = cur.prev, cur.next, cur.next

        self.head = prev
        return self.head

    # =============================================================

    def rotate(self, n: int, dir: str='right') -> Node:
        """
        Rotate linked list with the direction right or left
        """
        # (base case)
        if not self.head or not self.head.next: return self.head

        # (1) Get tail node and find the length
        length, tail = 1, self.head
        while tail.next: length, tail = length+1, tail.next

        # (2) Check rotate in a cycle
        n %= length
        if n == 0: return self.head

        # (3) Calculate the number of rotation 
        if   dir == 'right': rotation = length - n - 1
        elif dir == 'left':  rotation = n - 1

        # (4) Get new tail node
        newTail = self.head
        for _ in range(rotation): newTail = newTail.next

        tail.next, self.head.prev = self.head, tail
        self.head = newTail.next
        newTail.next.prev, newTail.next = None, None

        return self.head

    # =============================================================

    def removeDuplicate(self) -> Node:
        """
        Remove nodes with duplicate values
        """
        # (base case)
        if not self.head or not self.head.next: return self.head

        cur = self.head
        while cur:
            # (1) Modify next pointer
            while cur.next and cur.data == cur.next.data:
                cur.next = cur.next.next
            
            # (2) Modify prev pointer
            if cur.next: cur.next.prev = cur
            
            # (3) Move current node
            cur = cur.next

        return self.head


if __name__ == '__main__':
    l1 = LinkedList()
    for data in ['A', 'B', 'C']: l1.append(data)
    print(f'\n[List 1]    {l1}')                                            # ABC
    print(f'[Length]    {len(l1)}');    l1.summary()                        # 3
   
    print('\nInsert "D" before "B"')
    l1.insertBefore('D', 'B');          l1.summary()                        # ADBC
    
    print('\nInsert "E" after "B"')
    l1.insertAfter('E', 'B');           l1.summary()                        # ADBEC
    
    print('\nDelete "D"')
    l1.delete('D');                     l1.summary()                        # ABEC
    
    print('\nDelete "E"')
    l1.delete('E');                     l1.summary()                        # ABC
    
    print('\nDelete "A"')
    l1.delete('A');                     l1.summary()                        # BC
    
    print('\nDelete "C"')
    l1.delete('C');                     l1.summary()                        # B

    print('\nAppend "C"')
    l1.append('C');                     l1.summary()                        # BC

    print('\nPrepend "C"')
    l1.prepend('A');                    l1.summary()                        # ABC

    print('\nReverse')
    l1.reverse();                       l1.summary()                        # CBA

    print('\nPrepend "C"')
    l1.prepend('C');                    l1.summary()                        # CCBA

    print('\nAppend "A"')
    l1.append('A');                     l1.summary()                        # CCBAA

    print('\nInsert "B" after "B"')
    l1.insertAfter('B', 'B');           l1.summary()                        # CCBBAA

    print('\nInsert "B" after "B"')
    l1.insertAfter('B', 'B');           l1.summary()                        # CCBBBAA

    print('\nRemove dueplicates')
    l1.removeDuplicate();               l1.summary()                        # CBA

    print('\nReverse')
    l1.reverse();                       l1.summary()                        # ABC

    print('\nAppend "D"')
    l1.append('D');                     l1.summary()                        # ABCD

    print('\nRotate right for 2 times')
    l1.rotate(2, dir='right');          l1.summary()                        # CDAB

    print('\nRotate left for 2 times')
    l1.rotate(2, dir='left');           l1.summary()                        # ABCD