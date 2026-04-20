class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        hashmap = {}
        #time complexity of this funtion is O(n * mlog(m))
        #O(n)
        for word in strs:
            #Sorts are O(mlog(m))
            sorted_word = ("").join(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = []
            hashmap[sorted_word].append(word)
        #O(n)
        for key, value in hashmap.items():
            final.append(value)
        return final
            



                

            

        