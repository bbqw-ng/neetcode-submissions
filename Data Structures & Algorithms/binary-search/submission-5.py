class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = low + (high-low) // 2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                low = middle + 1
            elif target < nums[middle]:
                high = middle - 1
        return -1
