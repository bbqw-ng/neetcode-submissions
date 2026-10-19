# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #we need to take the midpoint with fast and slow pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #then we need to reverse the right side of the mid pointer
        #takesthe right side
        curr = slow.next
        #disconnects it from the left
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        #then we need to interleave them
        curr1 = head
        curr2 = prev
        #we take the smaller array as our condition
        while curr2:
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2

                




            
            
