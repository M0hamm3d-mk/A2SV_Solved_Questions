# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        new_node = ListNode(head.val)
        curr = head.next
        prev = head
        while curr:
            new_node = ListNode(curr.val,new_node)
            curr = curr.next
        return new_node