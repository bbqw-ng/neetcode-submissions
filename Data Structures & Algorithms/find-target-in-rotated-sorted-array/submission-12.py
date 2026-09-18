class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0 
        r = n - 1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                #means that pivot point is on the left side
                r = m
            else:
                #we do m+1 here because we are side that is after mid
                l = m + 1
        #min_ele is not a value it is an index, if the min value lives at index 0, that means the array is sorted
        #we do regular bin seartch
        min_ele = l
        if min_ele == 0:
            l,r = 0, n-1
        elif target >= nums[0] and target <= nums[min_ele - 1]:
            l,r = 0, min_ele - 1
        elif target >= nums[min_ele] and target <= nums[n-1]:
            l,r = min_ele, n-1

        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1




            

                
                
                
                

