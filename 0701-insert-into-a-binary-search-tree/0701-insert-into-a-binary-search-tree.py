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
                if not r.right:
                    r.right = TreeNode(v)
                    return root
                return insert(r.right,val)
            else:
                if not r.left:
                    r.left = TreeNode(v)
                    return root
                return insert(r.left,v)
        return insert(root,val)
