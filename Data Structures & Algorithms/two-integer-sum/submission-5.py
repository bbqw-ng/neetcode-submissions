class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_list = []
        for num in range((len(nums))):
            numberToLookFor = target - nums[num]
            if numberToLookFor in nums and nums.index(numberToLookFor) is not num:
                if num > nums.index(numberToLookFor):
                    return_list.append(nums.index(numberToLookFor))
                    return_list.append(num)
                else:
                    return_list.append(num)
                    return_list.append(nums.index(numberToLookFor))
                return return_list
            
