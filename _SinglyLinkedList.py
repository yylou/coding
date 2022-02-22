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
            while head:
                self.append(head.data)
                head = head.next

    def get_node(self, key) -> Node:
        """
        Retrieve node by key (data)
        """
        cur = self.head
        while cur: 
            if cur.data == key: return cur
            cur = cur.next

        return None

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

    # =============================================================

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

    def prepend(self, data) -> Node:
        """
        Add new node to the head of the linked list
        """
        new = Node(data, self.head)
        self.head = new

        return self.head

    def insert_after(self, node, data) -> Node:
        """
        Add new node after the specific node
        """
        new = Node(data)
        new.next = node.next
        node.next = new

        return self.head

    def delete(self, key) -> Node:
        """
        Delete node by searching key as node's data
        """
        cur = self.head

        # Node to be deleted is head
        if cur.data == key:
            self.head = cur.next
            cur = None

        # Search for the node to be deleted
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

    def get_len_iterative(self) -> int:
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

    # =============================================================

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

    # =============================================================

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

    # =============================================================

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
        node = self.head

        tail, length = node, 1
        while tail.next: tail, length = tail.next, length + 1

        n %= length
        if n == 0: return node

        # Find new tail node
        if   dir == 'right': rotation = length - n - 1
        elif dir == 'left':  rotation = n - 1

        new_tail = node    
        for _ in range(rotation): new_tail = new_tail.next

        self.head = new_tail.next
        tail.next, new_tail.next = node, None

        return self.head

    # =============================================================

    def get_middle(self) -> Node:
        """
        Get the middle node of the linked list
        """
        # (base case)
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

    def split(self, n=2) -> tuple:
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

    # =============================================================

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

    # =============================================================

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


if __name__ == '__main__':
    l1 = LinkedList()
    l1.append('B')
    l1.prepend('A')
    l1.insert_after(l1.get_node('B'), 'C')
    l1.insert_after(l1.get_node('C'), 'D')
    print(f'\n[List 1]    {l1}')                # ABCD
    length = l1.get_len_iterative()
    print('Length:    ', length)                # 4

    l1.delete('B')
    print(f'Remove B:   {l1}')                  # ACD
    tmp = l1.delete('E')
    print(f'Remove E:   {l1}')                  # ACD

    l2 = LinkedList(l1.insert_after(l1.get_node('A'), 'B'))
    print(f'\n[List 2]         {l2}')           # ABCD
    l2.delete_pos(2)
    print(f'Remove 2nd node: {l2}')             # ABD
    l2.delete_pos(7)
    print(f'Remove 7th node: {l2}')             # ABD
    
    length = l2.get_len_iterative()
    print(f'Length (iter):     {length}')       # 3
    length = l2.get_len_recursive(l2.head)
    print(f'Length (recu):     {length}')       # 3

    print(f'\n[List 1]        {l1}')            # ABCD
    l1.swap_data('A', 'C')
    print(f"Swap 'A' & 'C': {l1}")              # CBAD
    l1.swap_data('C', 'D')
    print(f"Swap 'C' & 'D': {l1}")              # DBAC
    l1.swap_data('B', 'C')
    print(f"Swap 'B' & 'C': {l1}")              # DCAB
    tmp = l1.swap_data('A', 'B')
    print(f"Swap 'A' & 'B': {l1}")              # DCBA

    l1.reverse_iterative()
    print(f'Reverse:        {l1}')              # ABCD
    l1.reverse_recursive()
    print(f'Reverse:        {l1}')              # DCBA

    l1.rotate(2, dir='right')
    print(f'Rotate right 2: {l1}')              # BADC
    tmp = l1.rotate(2, dir='left')
    print(f'Rotate left  2: {l1}')              # DCBA

    l2 = LinkedList()
    l2.append('E')
    l2.append('F')
    l2.append('G')
    l2.append('H')                              # EFGH

    print(f'\n[List 1]        {l1}')            # DCBA
    print(  f'[List 2]        {l2}')            # EFGH
    l3 = LinkedList(mergeTwoLists_recursive(l1.head, l2.head))
    print(f'Merge:      {l3}')                  # DCBAEFGH

    l1 = LinkedList()
    l1.append('A')
    l1.append('B')
    l1.append('G')
    l1.append('H')

    print(f'\n[List 1]        {l1}')            # ABGH
    print(  f'[List 2]        {l2}')            # EFGH
    l3 = LinkedList(mergeTwoLists_recursive(l1.head, l2.head))
    print(f'Merge:      {l3}')                  # ABEFGGHH

    l3.removeDuplicate_set()
    print(f'Remove Dup: {l3}')                  # ABEFGH

    l3.insert_after(l3.get_node('A'), 'A')
    l3.insert_after(l3.get_node('A'), 'A')
    l3.insert_after(l3.get_node('G'), 'G')
    l3.insert_after(l3.get_node('H'), 'H')

    print(f'\n[List 3]      {l3}')              # AAABEFGGHH
    l5 = LinkedList(l3.removeDuplicate_ifSorted())
    print(f'Remove Dup:   {l3}')                # ABEFGH
    length = l3.get_len_iterative()
    print(f'Length (recu):     {length}')       # 6
    print(f'[Remove 6-th last node: {l3.get_nthToLast(6)}]')
    l4 = LinkedList(l3.remove_nthToLast(6))
    print(f'[List 3]       {l3}')               # ABEFGH
    
    print(f'\n[List 4]       {l4}')             # BEFGH
    length = l4.get_len_iterative()
    print(f'Length (recu):     {length}')       # 5
    print(f'[Get 3-th last node] {l4.get_nthToLast(3)}')
    print(f'[Get 7-th last node]')
    node = l4.get_nthToLast(7)
    print(f'[Remove 6-th last node]')
    l4.remove_nthToLast(6)
    
    print(f'\n[List 4]       {l4}')             # BEFGH
    print(f'[Remove 1-th last node: {l4.get_nthToLast(1)}]')
    l4.remove_nthToLast(1)
    print(f'[List 4]       {l4}')               # BEFG

    for _ in range(4): l5.remove_nthToLast(1)
    for char in ['C', 'D', 'E']: l5.append(char)
    for char in ['1', '2', '3', '4', '5']: l5.append(char)
    print(f'\n[List 5]       {l5}')             # AAABEFGGHH
    l6 = LinkedList(l5.head)
    length = l5.get_len_iterative()
    print(f'Length:        {length}')           # 6
    print(f'Middle Node:   {l5.get_middle()}')  # 1
    first, second = l5.split()
    first, second = LinkedList(first), LinkedList(second)
    print(f'1st Part:      {first}')
    print(f'2nd Part:      {second}')

    l6.remove_nthToLast(6)
    print(f'\n[List 6]       {l6}')             # BEFGH
    length = l6.get_len_iterative()
    print(f'Length:        {length}')           # 5
    print(f'Middle Node:   {l6.get_middle()}')  # 1
    first, second = l6.split()
    first, second = LinkedList(first), LinkedList(second)
    print(f'1st Part:      {first}')
    print(f'2nd Part:      {second}')