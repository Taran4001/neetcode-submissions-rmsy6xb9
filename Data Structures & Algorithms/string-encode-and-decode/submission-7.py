class Solution:

    def encode(self, strs: List[str]) -> str:
        res = list()
        for string in strs:
            res.append(str(len(string)) + "#" + string)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        strs = list()
        i = 0
        while i < len(s):
            j = i
            strLen = list()
            while s[j].isdigit():
                strLen.append(s[j])
                j += 1
            strs.append(s[j + 1:int("".join(strLen)) + j + 1])
            i = int("".join(strLen)) + j + 1

        
        return strs