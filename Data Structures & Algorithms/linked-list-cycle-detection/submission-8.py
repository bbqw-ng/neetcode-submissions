# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        #if while loop breaks out, that means f is currently None so we don't have a cycle
        return False


