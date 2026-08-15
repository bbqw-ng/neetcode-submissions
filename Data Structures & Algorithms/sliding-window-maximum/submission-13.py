class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        if k == 1:
            return nums
        step_max = []
        max_heap = []
        left, right = 0, 0
        while right < len(nums):
            heapq.heappush(max_heap, (-nums[right], right))
            #fix this conditional here, since we need to account for smaller array sizes
            #this conditional only works if right gets large enough first
            if right == left + k - 1:
                max_ele = max_heap[0]
                while max_ele[1] < left:
                    #remove out of bounds highest
                    heapq.heappop(max_heap)
                    #grab newest highest
                    max_ele = max_heap[0]
                step_max.append(-max_ele[0])
                left += 1
            right += 1
        return step_max
