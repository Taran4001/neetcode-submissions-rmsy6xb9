class Solution:

    def encode(self, strs: List[str]) -> str:
        res = list()
        for string in strs:
            res.append(str(len(string)) + "#" + string)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = list()
        while i < len(s):
            j = i
            wordLen = list()
            while s[j].isdigit():
                wordLen.append(s[j])
                j += 1
            wordLen = "".join(wordLen)
            wordLen = int(wordLen)
            res.append(s[j + 1:j + wordLen + 1])
            i = j + wordLen + 1
        
        return res
            
