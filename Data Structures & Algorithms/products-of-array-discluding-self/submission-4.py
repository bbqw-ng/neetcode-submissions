class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[index] = num

        i = 0
        while (i < len(nums)):
            product = 1
            for key, value in hashmap.items():
                if key != i:
                    product *= value 
            output.append(product)
            i += 1
        return output
                
            
