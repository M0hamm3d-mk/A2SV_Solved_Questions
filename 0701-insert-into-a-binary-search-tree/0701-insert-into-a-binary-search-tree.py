# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(r,v):
            if not r:
                return TreeNode(v)
            if r.val < v:
                r.right =  insert(r.right,v)
            else:
                r.left =  insert(r.left,v)
            return r
        return insert(root,val)
