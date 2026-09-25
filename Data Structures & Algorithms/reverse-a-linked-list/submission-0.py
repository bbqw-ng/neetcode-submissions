# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        curr = head
        while curr.next != None:
            #saving next in linked
            temp = curr.next
            #setting curr next to previous (flipping order)
            curr.next = prev
            #setting previous to current 
            prev = curr
            #setting curr to the next node
            curr = temp
        curr.next = prev
        prev = curr
        return prev
