class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}*"
            encoded += word
        print(encoded)
        return encoded
            
    def decode(self, s: str) -> List[str]:
        decoded = list()
        #two pointer prob
        i = 0
        while (i < len(s)):
            j = i
            while (s[j] != "*"):
                #increments j until it hits the delim
                j += 1
            #find out the length of the word,
            word_len = int(s[i:j])
            print(word_len)
            #reposition i to the beginning of the word
            i = j + 1
            #extract the word
            word = s[i:i+word_len]
            #add to decoded list
            decoded.append(word)
            #reposition i to the index after the word and continue on
            i = i + word_len
        return decoded


