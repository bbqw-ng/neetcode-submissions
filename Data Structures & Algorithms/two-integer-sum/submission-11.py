class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        #looking for an i j pair that satisfies condition
        for index, i in enumerate(nums):
            j = target - i
            if j in hm and hm[j] != index:
                return [hm[j], index]
            hm.setdefault(i, index)
            

                


                


