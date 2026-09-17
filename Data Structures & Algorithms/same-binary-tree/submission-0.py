# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recursion(p,q):
            if p is None and q is None:
                return True

            if (p is None and q is not None) or (q is None and p is not None):
                return False
            
            if p.val != q.val:
                return False

            return recursion(p.left,q.left) and recursion(p.right,q.right)

        return recursion(p,q)