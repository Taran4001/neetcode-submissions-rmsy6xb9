class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.countCh(s) == self.countCh(t)

    
    def countCh(self, string: str) -> dict:
        chCount = dict()
        
        for ch in string:
            chCount[ch] = chCount.get(ch, 0) + 1
        
        return chCount