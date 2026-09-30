# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        parentMap = {}
        startNode = None

        if root is None:
            return 0

        def dfs(node, parent):
            nonlocal startNode

            if node is None:
                return

            parentMap[node] = parent

            if node.val == start:
                startNode = node

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        visited = set()
        max_time = 0

        def burn(node, time):
            nonlocal max_time

            if node is None or node in visited:
                return

            visited.add(node)
            max_time = max(max_time, time)

            burn(node.left, time + 1)
            burn(node.right, time + 1)
            burn(parentMap[node], time + 1)

        burn(startNode, 0)

        return max_time