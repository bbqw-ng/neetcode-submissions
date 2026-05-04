class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        #takes the smaller num of the two, multiplies by #'s in between including the smaller num 
        best_max = 0
        while l < r: 
            #examples: index 9 - index 3 = 6 inbetween including biggest already
            curr_max = min(heights[l], heights[r]) * (r-l)
            if curr_max > best_max: 
                best_max = curr_max
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return best_max

