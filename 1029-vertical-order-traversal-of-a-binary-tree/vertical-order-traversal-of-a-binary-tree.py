# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
         
        if root is None:
            return []
        mp = {}
        def dfs(node,hd,level):
            if node is None:
                return
            if hd not in mp:
                mp[hd] = []

            mp[hd].append((level,node.val))

            dfs(node.left,hd - 1,level + 1)
            dfs(node.right,hd + 1, level + 1)
        
        dfs(root, 0, 0)
        ans = []
        for hd in sorted(mp):
            # mp[hd].append((level, node.data)) -> this not bc df's has ended
            column = []
            for item in sorted(mp[hd]):
                column.append(item[1])   

            ans.append(column)
        return ans

