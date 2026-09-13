class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_time = max(piles)
        min_time = max_time
        start = 1
        end = max_time
        while start <= end:
            mid = start + (end - start) // 2
            count = 0
            for pile in piles:
                #rounds up unlike floor division with  '//'
                count += math.ceil(pile / mid)
            if count <= h:
                end = mid - 1
                min_time = mid
                #mid is valid, end = mid
            elif count > h:
                start = mid + 1
                #mid is invalid, have to upper the bounds since that means we are eating too slow we need to increase!
        return min_time

            
            




            

