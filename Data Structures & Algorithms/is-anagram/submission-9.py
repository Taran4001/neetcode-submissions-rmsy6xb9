class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countChS = dict()
        countChT = dict()
        for ch in s:
            countChS[ch] = countChS.get(ch, 0) + 1
        for ch in t:
            countChT[ch] = countChT.get(ch, 0) + 1
        
        return countChS == countChT