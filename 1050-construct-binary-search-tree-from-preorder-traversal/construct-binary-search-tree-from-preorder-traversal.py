# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        index = 0

        def build(low, high):
            nonlocal index

            if index == len(preorder):
                return None
            
            if preorder[index] <= low or preorder[index] >= high:
                return None
            
            node = TreeNode(preorder[index])
            index += 1

            node.left = build(low, node.val)
            node.right = build(node.val, high)

            return node
        
        return build(float("-inf"), float("inf"))