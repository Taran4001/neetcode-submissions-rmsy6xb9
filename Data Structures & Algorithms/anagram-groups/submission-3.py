from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for string in strs:
            key = [0] * 26
            for ch in string:
                key[ord(ch) - ord("a")] += 1
            hashMap[tuple(key)].append(string)
        
        return list(hashMap.values())