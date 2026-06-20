# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def go(r):
            if not r:
                return 0
            else:
                return 1 + go(r.left) + go(r.right)
        return go(root)