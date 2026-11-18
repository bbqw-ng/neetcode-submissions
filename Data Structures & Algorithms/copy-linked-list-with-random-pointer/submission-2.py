"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        hm: {old 3:new 3, old 7, new 7, old 4, new 4}
        no random pointers for the new nodes have been implemented yet.
        new's random = old nodes associated new node.
        new 3 random = node of old 3.random = a key to the old rnaomd node, and when we take the val of that old rand node, we get the new node therefore we map the new node to its new random node.
        '''
        h = head
        output = None
        hm = {}
        while h:
            new_node = Node(h.val)
            if not output:
                output = new_node
            hm[h] = new_node
            h = h.next
        
        for index, (old, new) in enumerate(hm.items()):
            new.next = hm[old.next] if old.next else None
            new.random = hm[old.random] if old.random else None
        return output
