# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        self.finalMax(root)
        return self.maxi

    def finalMax(self, node):
        if node is None:
            return 0
        lh = self.finalMax(node.left)
        rh = self.finalMax(node.right)

        self.maxi = max(self.maxi, lh + rh)

        return 1 + max(lh,rh)