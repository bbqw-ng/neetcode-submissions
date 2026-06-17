class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        most_freq = 0
        hm = {}
        l,r = 0,0
        while r < len(s):
            r_char = s[r]
            #adding char to dictionary
            if r_char not in hm:
                hm[r_char] = 1
            else:
                hm[r_char] += 1
            #ok so we dont do anything to k here because k is already included in the substring because our "r" pointer includes k in sizing when it moves
            #getting the longest combo and the greatest freq
            most_freq = max(most_freq, hm[r_char])
            while ((r-l+1)-most_freq > k):
                l_char = s[l]
                #l_char should already be in map since r_char passes through it
                hm[l_char] -= 1
                #increment the actual l to reduce the size of feasbile substring to match with k
                l += 1
                most_freq = max(most_freq, hm[l_char])
            #r-l+1 -> the size of the substring so if 0,0 that means the length is 1 cuz the smallest substring you can have is 1 letter
            longest = max(longest, r-l+1)
            r += 1

                
        return longest

            

            


        
        
        