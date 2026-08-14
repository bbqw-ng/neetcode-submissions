class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if "".join(sorted(s)) == "".join(sorted(t)):
            return s
        hm = {}
        hm_c = {}
        for char in t:
            hm.setdefault(char, 0)
            hm_c.setdefault(char,0)
            hm[char] += 1

        result = ""
        valid = 0
        l,r = 0,0
        while r < len(s):
            if s[r] in hm_c:
                hm_c[s[r]] += 1
                if hm_c[s[r]] == hm[s[r]]:
                    valid += 1
            r += 1
            while valid == len(hm):
                if s[l] in hm_c:
                    hm_c[s[l]] -= 1
                    if hm_c[s[l]] < hm[s[l]]:
                        valid -= 1
                    if result == "" or len(result) > len(s[l:r]):
                        result = s[l:r]
                l += 1
        return result



        #need to implement something that checks the amount of duplicates needed 
            
                


            

