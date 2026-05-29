from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_group = defaultdict(list)
        for string in strs:
            str_char = [0] * 26
            for ch in string:
                str_char[ord(ch) - ord("a")] += 1
            anagrams_group[tuple(str_char)].append(string)
        
        return list(anagrams_group.values())
            