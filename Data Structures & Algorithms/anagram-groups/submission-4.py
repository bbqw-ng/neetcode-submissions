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
                #have a list in the value
                hashmap[sorted_word] = []
            #add every word into bucket
            hashmap[sorted_word].append(word)
        #O(n)
        for value in hashmap.values():
            final.append(value)
        return final
            



                

            

        