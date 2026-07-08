class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if self.checkPalindrome(s, i + 1, j) == True:
                    return True
                elif self.checkPalindrome(s, i, j - 1) == True:
                    return True
                else: 
                    return False
            else:
                i += 1
                j -= 1
        return True

    def checkPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True