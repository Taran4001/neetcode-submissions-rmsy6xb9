class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordLen = 0
        i = len(s) - 1
        while i > -1 and s[i] == " ":   
            i -= 1  
        while i > -1 and s[i] != " ": 
            wordLen += 1
            i -= 1
        return wordLen