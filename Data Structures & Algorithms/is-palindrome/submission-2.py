class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = list()
        for char in s:
            if char.isalnum(): 
                cleaned.append(char.lower())
            print(cleaned)
        return "".join(cleaned)[::-1] == "".join(cleaned)
