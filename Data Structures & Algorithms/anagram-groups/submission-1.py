class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        hashmap = {}
        #time complexity of this funtion is O(n * mlog(m))
        #O(n)
        for word in strs:
            #Sorts are O(mlog(m))
            sorted_word = ("").join(sorted(word))
            print(sorted_word)
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [word]
                print(hashmap[sorted_word])
            else:
                hashmap[sorted_word].append(word)
                print(hashmap[sorted_word])
        #O(n)
        for key, value in hashmap.items():
            print(key)
            print(value)
            final.append(value)
        return final
            



                

            

        