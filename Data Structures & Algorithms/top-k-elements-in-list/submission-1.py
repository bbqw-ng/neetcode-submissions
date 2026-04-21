class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        sorted_nums = sorted(hashmap.items(), key=lambda values: values[1], reverse=True)
        freq = []
        for i in range(k):
            freq.append(sorted_nums[i][0])
        print(freq)
        return freq

            

