class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i > -1 and not s[i].isalpha():
            i -= 1
        j = i
        while i > -1 and s[i].isalpha():
            i -= 1
        
        return len(s[i + 1: j + 1])
        

