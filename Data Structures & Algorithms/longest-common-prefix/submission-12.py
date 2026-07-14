class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = list()
        for ch in range(len(strs[0])):
            for string in strs:
                if len(string) <= ch or strs[0][ch] != string[ch]:
                    return "".join(res)
            res.append(strs[0][ch])

        return "".join(res)