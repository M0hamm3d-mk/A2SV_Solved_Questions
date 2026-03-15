# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        stack = [dummy]
        curr = head
        while curr :
            while stack and curr.val > stack[-1].val:
                stack.pop()
            if stack:   
                stack[-1].next = curr
            stack.append(curr)
            curr = curr.next
        return stack[0] if stack else head