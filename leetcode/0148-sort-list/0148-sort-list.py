# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1,l2):
            if not l2:
                return l1
            if not l1:
                return l2
            if l1.val > l2.val:
                l2.next = merge(l1,l2.next)      
                return l2
            else:
                l1.next = merge(l1.next,l2)
                return l1

        def mergeSort(left,right):
            if not left or left == right:
                return left
            
            if left.next == right:
                if left.val > right.val:
                    left.val,right.val = right.val,left.val
                return left
                
            
            # mid = ListNode()
            fast = mid = left
            while fast and fast.next:
                mid = mid.next
                fast = fast.next.next
            
            temp = mid.next 
            mid.next = None
                    
            return merge(mergeSort(left,mid), mergeSort(temp,right))
        
        curr = head
        while curr and curr.next:
            curr = curr.next
        return mergeSort(head,curr)
            