# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def rightSideView(self, level=0, result = None, root: TreeNode | None) -> list[int]:
class Solution:
    def rightSideView(self, root, level=0, result=None):
        if result is None:
            result = []
        
        if root is None:
            return result
        
        if level == len(result):
            result.append(root.val)
        
        self.rightSideView(root.right, level + 1, result)
        self.rightSideView(root.left, level + 1, result)

        return result