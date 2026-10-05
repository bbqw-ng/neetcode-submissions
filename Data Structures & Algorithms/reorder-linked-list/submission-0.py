# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find midpoint with slow and fast pointer
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #grabbing the midpoitn
        mp = slow.next
        #setting next to None
        slow.next = None

        #reversing 2nd half LL
        prev = None
        curr = mp 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #merging LL
        curr1 = head
        curr2 = prev
        while curr2:
            next1 = curr1.next
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1 = next1
            curr2 = next2





        

        