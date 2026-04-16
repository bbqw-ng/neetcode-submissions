class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            hashmap = {}
            for num in nums:
                if num not in hashmap:
                    hashmap[num] = 1
                else:
                    return True
        return False
        