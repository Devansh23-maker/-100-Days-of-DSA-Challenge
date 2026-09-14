# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        self.solve(root)
        return self.maxi
    
    def solve(self, node):
        if node is None:
            return 0
        
        left = max(0, self.solve(node.left))
        right = max(0, self.solve(node.right))

        self.maxi = max(self.maxi, node.val + left +right)
        
        return node.val + max(left, right)