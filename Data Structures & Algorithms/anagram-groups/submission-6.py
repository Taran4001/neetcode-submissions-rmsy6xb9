from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        subStrings = defaultdict(list)
        for string in strs:
            countCh = [0] * 26
            for ch in string:
                countCh[ord(ch) - ord("a")] += 1
            subStrings[tuple(countCh)].append(string)
        return list(subStrings.values())