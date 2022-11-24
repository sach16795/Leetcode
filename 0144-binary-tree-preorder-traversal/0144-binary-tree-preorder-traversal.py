# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        pre = []
        q = []
        
        while curr is not None or len(q) > 0:
            while curr is not None:
                pre.append(curr.val)
                q.append(curr.right)
                curr = curr.left
            curr = q.pop()
        return pre
            