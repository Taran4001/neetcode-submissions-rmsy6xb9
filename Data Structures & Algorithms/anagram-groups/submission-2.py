class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for ch in string:
                key[ord(ch) - ord("a")] += 1
            res[tuple(key)].append(string)
        return list(res.values()) 