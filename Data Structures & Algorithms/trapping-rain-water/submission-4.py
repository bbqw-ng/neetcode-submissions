class Solution:
    def trap(self, height: List[int]) -> int:
        #approach -> checks the maxes, add each max at anyt position into l and r to compare min numbers in that position, 
        #sub smaller number from actual height to get area
        total = 0
        #initialize maxes as 0
        l_max = r_max = 0
        l_arr = list()
        r_arr = list()
        for i in range(len(height)):
            #j is for working backwards
            #0 index it and then take away i
            j = len(height) - 1 - i
            l_arr.append(l_max)
            r_arr.append(r_max)
            if height[i] > l_max:
                l_max = height[i]
            if height[j] > r_max:
                r_max = height[j]
        # we do not declare the size of the array and are appending it at the front, so we need to reverse.
        r_arr.reverse()
        
        for i in range(len(height)):
            smaller = min(l_arr[i], r_arr[i])
            total += max(0, smaller - height[i])

        return total

                