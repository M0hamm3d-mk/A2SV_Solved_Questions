# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def searchAndDelete(r,k):
            if not r:
                return None
            if r.val > k:
                r.left = searchAndDelete(r.left,k)
            elif r.val < k:
                r.right = searchAndDelete(r.right,k)
            else:
                if not r.left:
                    return r.right
                if not r.right:
                    return r.left

                curr = r.right

                while curr.left:
                    curr = curr.left
                r.val = curr.val
                r.right = searchAndDelete(r.right,curr.val)
            return r
        return searchAndDelete(root,key)
            