from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root : return []

        queue = deque([(root,0)])
        mapp = {}

        while queue:
            node , row = queue.popleft()

            if row in mapp:
                mapp[row].append(node.val)
            else:
                mapp[row] = [node.val]


            if node.left:
                queue.append((node.left,row+1))

            if node.right:
                queue.append((node.right,row+1))
        
        result = []
        for row in sorted(mapp):
            result.append(mapp[row])
        return result