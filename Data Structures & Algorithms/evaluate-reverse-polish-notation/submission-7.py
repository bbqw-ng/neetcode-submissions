class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations_dict = {"+": lambda x,y :x+y,
        "*": lambda x,y :x*y,
        "/": lambda x,y : int(x/y),
        "-": lambda x,y : x-y}

        num_stack = []
        i = 0
        while i < len(tokens):
            token = None
            try: 
                token = int(tokens[i])
                num_stack.append(token)
            except:
                token = tokens[i]

                first = num_stack.pop()
                second = num_stack.pop()
                #second is first param since its our original numbers' operations.
                result = operations_dict[token](second, first)
                num_stack.append(result)
            i += 1
        return num_stack.pop()

            
        