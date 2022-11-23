from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Approach 2: Iteration
        def check (p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p,q)])
        
        while deq:
            p,q = deq.popleft()
            if not check(p,q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True
        
        # Approach 1: Recursion
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        # else:
        #     return self.isSameTree (p.left, q.left) and self.isSameTree(p.right, q.right)