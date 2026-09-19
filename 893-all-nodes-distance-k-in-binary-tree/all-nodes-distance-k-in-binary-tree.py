# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root, target, k):
        self.parent_map = {}
        self.build_parent_map(root, None, self.parent_map)
        
        result = []
        visited = set()
        self.dfs(target, visited, 0, k, result)
        return result
    
    def build_parent_map(self, node, parent, parent_map):
        if node is None:
            return
        parent_map[node] = parent
        self.build_parent_map(node.left, node, parent_map)
        self.build_parent_map(node.right, node, parent_map)
    
    def dfs(self, node, visited, distance, k, result):
        if node is None or node in visited:
            return
        
        visited.add(node)
        
        if distance == k:
            result.append(node.val)
            return
        
        self.dfs(node.left, visited, distance + 1, k, result)
        self.dfs(node.right, visited, distance + 1, k, result)
        self.dfs(self.parent_map.get(node), visited, distance + 1, k, result)