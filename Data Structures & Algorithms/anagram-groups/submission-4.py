class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            chCount = [0] * 26
            for ch in string:
                chCount[ord(ch) - ord("a")] += 1
            res[tuple(chCount)].append(string)

        return list(res.values())
