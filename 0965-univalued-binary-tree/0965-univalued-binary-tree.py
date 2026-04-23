# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        v = root.val
        while q:
            root = q.popleft()
            if root.val != v:
                return False
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        return  True

