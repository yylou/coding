"""
Author  : Yuan-Yao Lou (Mike)
Title   : PhD student in ECE at Purdue University
Email   : yylou@purdue.edu
Website : https://yylou.github.io/
Date    : Feb 17, 2023

Project :
    [Coding practice] Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        #   | Level-order Traversal
        ret = []
        stack = [(self, 0)]
        while stack:
            node, level = stack.pop()
            
            if level == len(ret): ret.append([])
            if node:
                ret[level].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left,  level + 1))
            else:
                ret[level].append(None)
        
        return str(ret[:-1])

class Tree:

    @classmethod
    def search(self, id: str):
        for function, object in self.__dict__.items():
            if function[1:5] == id: return object
        return None

    @classmethod
    def _0100_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        def iterative(p, q):
            """  Easy  |  Iterative  """
            # Time:  O(n)
            # Space: O(n)

            stack1, stack2 = [p], [q]
            while stack1 and stack2:
                n1, n2 = stack1.pop(), stack2.pop()
                if not n1 and not n2: continue
                if not n1  or not n2: return False
                if n1.val != n2.val: return False

                stack1.append(n1.right)
                stack2.append(n2.right)
                stack1.append(n1.left)
                stack2.append(n2.left)

            return True
        
        def recursive(p, q):
            """  Easy  |  Recursive  """
            # Time:  O(n)
            # Space: O(n)

            if not p and not q: return True
            if not p  or not q: return False
            if p.val != q.val: return False

            return recursive(p.left, q.left) and recursive(p.right, q.right)

        return recursive(p, q)

    @classmethod
    def _0102_binary_tree_level_order_traversal(self, root: TreeNode) -> str:
        """  Medium  |  Pre-order traversal  """
        # Time:  O(n)
        # Space: O(n)

        ans = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if not node: continue

            if len(ans) == level: ans.append([])
            ans[level].append(node.val)
            stack.append((node.right, level + 1))
            stack.append((node.left,  level + 1))

        return ans

    @classmethod
    def _0110_balanced_binary_tree(self, root: TreeNode, val: int) -> TreeNode:
        """  Easy  |  Iterative  """
        # Time:  O(n)
        # Space: O(1)

        

    @classmethod
    def _0530_min_abs_diff_in_BST(self, root: TreeNode) -> int:
        """  Easy  |  Morris Traversal  |  (SAME AS 0783)"""
        # Time:  O(n)
        # Space: O(1)

        ans = float("inf")
        prev, cur = None, root
        while cur:
            if cur.left: 
                left = cur.left
                while left.right and left.right != cur:
                    left = left.right

                if left.right == cur:   # visited
                    left.right = None
                    if prev: ans = min(ans, abs(cur.val - prev.val))
                    prev, cur = cur, cur.right

                else:
                    left.right = cur
                    prev, cur = cur, cur.left

            else:   # no left child
                if prev: ans = min(ans, abs(cur.val - prev.val))
                prev, cur = cur, cur.right

        return ans
    
    @classmethod
    def _0701_insert_into_a_BST(self, root: TreeNode, val: int) -> TreeNode:
        def iterative(root, val):
            """  Medium  |  Iterative  """
            # Time:  O(n)
            # Space: O(1)

            if not root: return TreeNode(val)

            prev, cur = None, root
            while cur:
                if cur.val > val: prev, cur = cur, cur.left
                else: prev, cur = cur, cur.right
            
            if prev.val > val: prev.left = TreeNode(val)
            else: prev.right = TreeNode(val)

            return root
        
        def recursive(root, val):
            """  Medium  |  Recursive  """
            # Time:  O(n)
            # Space: O(n)

            if not root: return TreeNode(val)

            if root.val > val: root.left = recursive(root.left, val)
            else: root.right = recursive(root.right, val)
            return root

        return recursive(root, val)