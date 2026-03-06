# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even_ptr = head
        odd_ptr = head.next
        curr = odd_ptr.next
        start = odd_ptr
        n = 2
        while curr:
            if n % 2 :
                odd_ptr.next = curr
                odd_ptr = curr
            else:
                even_ptr.next = curr
                even_ptr = curr
            curr = curr.next
            n += 1
        odd_ptr.next = None
        even_ptr.next = start
        return head
        