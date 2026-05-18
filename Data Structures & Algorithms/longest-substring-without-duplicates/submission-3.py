class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #this sounds like a dynamic window problem, growing the window and checking the set
        if len(s) == 0:
            return 0
        out = 1
        for index, i in enumerate(s):
            r = index + 1
            sum = 1
            seen = set(i)
            while r <= len(s)-1:
                if s[r] in seen:
                    break
                seen.add(s[r])
                sum += 1
                r += 1
            out = max(sum, out)
        return out
            

            
        