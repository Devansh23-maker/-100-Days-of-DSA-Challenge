# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: TreeNode | None, queries: list[int]) -> list[list[int]]:
        arr = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        ans = []

        for query in queries:
            i = bisect_left(arr, query)

            # Floor
            if i < len(arr) and arr[i] == query:
                floor = arr[i]
            elif i > 0:
                floor = arr[i - 1]
            else:
                floor = -1

            # Ceil
            if i < len(arr):
                ceil = arr[i]
            else:
                ceil = -1

            ans.append([floor, ceil])

        return ans