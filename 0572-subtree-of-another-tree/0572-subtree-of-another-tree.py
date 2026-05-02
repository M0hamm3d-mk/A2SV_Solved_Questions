# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse(n1,n2):
            if not n1 and not n2:
                return True
            elif not n1:
                return False
            elif not n2:
                return False
            elif n1.val != n2.val:
                return False
            return traverse(n1.left,n2.left) and traverse(n1.right,n2.right)
            
    
        def go(n):
            if not n:
                return False
            elif  traverse(n,subRoot):
                return True
            return go(n.left) or go(n.right)
        # print('here')
        return go(root)
            