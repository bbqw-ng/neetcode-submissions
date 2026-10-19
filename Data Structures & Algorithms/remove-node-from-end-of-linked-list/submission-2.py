# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #fast and slow pointer, we move fast to n+1 first, then we move slow and fast togehter until fsat becomes none
        h = ListNode()
        h.next = head
        slow = fast = h
        for i in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return h.next
        
