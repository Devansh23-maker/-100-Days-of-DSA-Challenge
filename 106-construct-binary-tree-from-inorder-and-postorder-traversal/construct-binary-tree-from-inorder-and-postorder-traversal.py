# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        self.index_map = {value: idx for idx, value in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def build(in_left,in_right):
            if in_left > in_right:
                return None
        
            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)
            self.post_idx -= 1

            mid = self.index_map[root_val]
        
            root.right = build(mid + 1, in_right)
            root.left = build(in_left,mid - 1)
        

            return root

        return build(0, len(inorder) - 1)
