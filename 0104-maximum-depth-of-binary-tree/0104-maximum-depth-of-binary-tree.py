# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maximum_depth = 0
        self.depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if root:
                self.depth += 1
                self.maximum_depth = max(self.maximum_depth,self.depth)
                traverse(root.left)
                traverse(root.right)
                self.depth -= 1
            
        traverse(root)
        # self.maximum_depth = max(self.maximum_depth,self.depth)
        return self.maximum_depth   if root else 0