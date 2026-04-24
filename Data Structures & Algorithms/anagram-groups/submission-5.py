class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for word in strs:
            bucket = "".join(sorted(word))
            if bucket not in hm:
                hm.setdefault(bucket, [])
            hm[bucket].append(word)
        output = []
        for (key,value) in hm.items():
            output.append(value)
        return output

            



                

            

        