class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = list()
        nums.sort()
        for i, num in enumerate(nums):
            #if num is greater than 0 that means nothing to the right will make it 0 since right is bigger in sorted array
            if num > 0:
                break
            #make sure that num is not the same num as last time to avoid duplication if it is then we want to skip
            if i > 0 and num == nums[i-1]:
                continue
            #we loop through i, we have a fronty and back pointer front is currindex + 2 and back is len-1
            l = i + 1
            r = len(nums)-1
            #keep going until l and r meet then goto the next iteration
            while l < r:
                combined = num + nums[l] + nums[r]
                #declare what the number we need to find it  (must be in loop since it changes each time)
                #if the current num is smaller than the one we are looking for -> decrement right side (smaller numbers to the left)
                if combined < 0:
                    l += 1
                elif combined > 0:
                    r -= 1
                else:
                    output.append([num, nums[l], nums[r]])
                    #go to next variation
                    l += 1
                    r -= 1
                    #will keep skipping duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return output