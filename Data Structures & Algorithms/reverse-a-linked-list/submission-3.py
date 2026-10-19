# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head;
        prev = None
        while curr:
            #grab the next and set next to behind 
            temp = curr.next
            curr.next = prev

            #set next behind to current and current to next (flips it)
            prev = curr
            curr = temp
        #returns the end because thats now the head of the reversed linked list.
        return prev
        