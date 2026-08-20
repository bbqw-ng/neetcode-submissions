class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_stack = []
        right = len(temperatures) - 1
        while right >= 0:
            temp = temperatures[right]
            #if its the rightmost, automatic 0
            if right == len(temperatures) - 1:
                result[right] = 0
                temp_stack.append((right, temp))
                right -= 1
            elif temp >= temp_stack[-1][1]:
                temp_stack.pop()
                if not temp_stack:
                    result[right] = 0
                    temp_stack.append((right, temp))
                    right -= 1
            else:
                #print("current right", temperatures[right])
                #print(temp_stack[-1][0], temp_stack[-1][1])
                #print(right)
                result[right] = temp_stack[-1][0] - right
                temp_stack.append((right, temp))
                right -= 1
        return result
            





        
            
            