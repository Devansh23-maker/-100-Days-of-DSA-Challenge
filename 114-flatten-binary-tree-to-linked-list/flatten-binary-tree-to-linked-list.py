# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)

        left_flattened = root.left
        right_flattened = root.right

        root.left = None
        root.right = left_flattened
        
        curr = root
        while curr.right:
            curr = curr.right
        
        curr.right = right_flattened