#notes for improvement, instead of doing manual if else checks for brackets, we can map them using a hashmap to find key-value open-close pairs easier
#which would make it a lot easier to read and understand.
class Solution:
    def isValid(self, s: str) -> bool:
        open = ['[', '{', '(']
        if len(s) == 1:
            return False
        #declare a stack
        stack = []
        # we go through the list, adding any open brackets we see,
        for i in s:
            print(i)
            if i in open:
                stack.append(i)
        #if hit close bracket then we want to counter check the list to see if its a valid open (so we would check the last element in the stack)
            else:
                if not stack:
                    return False
                top = stack[-1]
                print(top)
                if i == ')' and top == '(':
                    stack.pop()
                elif i == ']' and top == '[':
                    print(i)
                    stack.pop()
                elif i == '}' and top == '{':
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
        #true: pop from stack, continue
        #false: return false, termiante immediately.






        