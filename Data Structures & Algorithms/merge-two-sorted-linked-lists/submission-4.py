# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(None)
        start = h
        while list1 and list2:
            if list1.val <= list2.val:
                h.next = list1
                list1 = list1.next
            else:
                h.next = list2
                list2 = list2.next
            h = h.next
        #instead of having these while loops we can do truthy opertaion this sees if list1 is a value that isnt none otherwise it goes for list2.
        h.next = list1 or list2
        return start.next
        """
        while list1:
            h.next = list1
            list1 = list1.next
            h = h.next
        while list2:
            h.next = list2
            list2 = list2.next
            h = h.next
        """
        
        