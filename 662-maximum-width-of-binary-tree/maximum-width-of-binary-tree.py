# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        self.max_width = 0
        self.level_first = {}

        def dfs(node, level, pos):
            if node is None:
                return
            
            if level not in self.level_first:
                self.level_first[level] = pos 
            
            self.max_width = max(self.max_width, pos - self.level_first[level] + 1)

            dfs(node.left, level + 1, 2 * pos)
            dfs(node.right, level + 1, 2 * pos + 1)
        
        dfs(root, 0 ,1)
        return self.max_width