# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Step 1: HashMap bana - O(1) lookup ke liye
        self.index_map = {value: idx for idx, value in enumerate(inorder)}
        self.pre_idx = 0  # preorder array mein "abhi kaunsa element process karna hai" track karega
        
        def build(in_left, in_right):
            # base case: agar range invalid hai (koi elements bache hi nahi is subtree ke liye)
            if in_left > in_right:
                return None
            
            # preorder ka current element hamesha ROOT hai
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1  # agla element agli baar ke liye aage badha do
            
            root = TreeNode(root_val)
            
            # inorder mein root ka index nikalo - O(1) via HashMap
            mid = self.index_map[root_val]
            
            # IMPORTANT: LEFT pehle banao (preorder order maintain karne ke liye)
            root.left = build(in_left, mid - 1)
            root.right = build(mid + 1, in_right)
            
            return root
        
        return build(0, len(inorder) - 1) 