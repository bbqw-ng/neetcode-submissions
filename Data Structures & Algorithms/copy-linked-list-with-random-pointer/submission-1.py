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
        #old node -> new Node
        hm = {}
        #creating new nodes for deep copy
        h = head
        while h:
            newNode = Node(h.val)
            hm[h] = newNode
            h = h.next

        prev = None
        for k, v in hm.items():
            #we calculate the random randomNodePointer
            #this points to a node
            newRandomPointer = k.random
            #find the node corresponding to random and set the new random node to the current node attribute
            if newRandomPointer == None:
                v.random = None
            else:
                v.random = hm[newRandomPointer]
            #we calculate the next
            if prev is not None:
                prev.next = v
            prev = v
        '''
        for k, v in hm.items():
            print(k.val)
            print(v.val)
            if v.next != None:
                print(v.next.val)
            else: print("None")
            if v.random != None:
                print(v.random.val)
            else: print("None")
            print("---------------")
        '''

        for k, v in hm.items():
            return v
