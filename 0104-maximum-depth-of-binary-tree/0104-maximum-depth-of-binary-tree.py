class Solution:
    def __init__(self,mx=0,depth=0):
        self.mx = mx
        self.depth = depth
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            self.depth += 1
            self.mx = max(self.mx,self.depth)
            self.maxDepth(root.left)
            self.maxDepth(root.right)
            self.depth -= 1
        return self.mx
        