class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(reverse=True)

        stack = []
        prev_curr_time = float('inf')
        for i in range(len(position)):
            curr_position = cars[i][0]
            curr_speed = cars[i][1]
            curr_time = (target - curr_position) / curr_speed
            if not stack:
                stack.append(curr_time)
            elif curr_time <= stack[-1]:
                #first car goes into stack, if next car's time is less than first car -> first car slower than next car
                #next car will catch up, which then forms a fleet
                #we want to continue meaning that we dont add it to the stack again because it is part of the fleet.
                continue
            else:
                stack.append(curr_time)
        return len(stack)

        
        
