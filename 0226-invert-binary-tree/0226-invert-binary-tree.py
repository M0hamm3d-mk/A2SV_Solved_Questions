# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r):
            if not r:
                return None
            else:
                r.left = dfs(r.left)
                r.right = dfs(r.right)
                r.left,r.right = r.right,r.left

            return r
        return dfs(root)