class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #find the window size -> len of s1
        window_size = len(s1)
        sorted_s1 = "".join(sorted(s1))
        i = 0
        max = len(s2)-window_size
        # to check if there is a permutation, we can sort both s1 and the window from s2 and then compare those for equliaty.
        while i <= max:
            #if s1 sorted is the same as s2 sorted, that means s2 is a permutation of s1 or is s1.
            if sorted_s1 == "".join(sorted(s2[i:i+window_size])):
                return True
            else:
                i += 1
        return False
        #if equal: true
        #else : false
        