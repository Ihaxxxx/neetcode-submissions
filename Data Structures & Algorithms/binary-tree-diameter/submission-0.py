class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node):
            nonlocal diameter

            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            diameter = max(diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)

        return diameter