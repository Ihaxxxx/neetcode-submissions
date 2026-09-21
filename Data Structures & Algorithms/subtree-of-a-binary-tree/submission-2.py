# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def SameTree(root1,root2):
            if root1 is None and root2 is None:
                return True
            
            if (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
                return False
            
            if root1.val != root2.val:
                return False

            return SameTree(root1.left,root2.left) and SameTree(root1.right,root2.right)

        def dfs(root):
            if root is None:
                return False
            if SameTree(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)

        return dfs(root)
        return equal
