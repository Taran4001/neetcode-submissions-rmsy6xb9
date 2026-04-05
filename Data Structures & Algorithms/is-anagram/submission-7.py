class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ch_count_s = dict()
        ch_count_t = dict()

        for ch in s:
            ch_count_s[ch] = ch_count_s.get(ch, 0) + 1
        
        for ch in t:
            ch_count_t[ch] = ch_count_t.get(ch, 0) + 1
        
        for ch in ch_count_t:
            if ch not in ch_count_s or ch_count_t[ch] != ch_count_s[ch]:
                return False
        
        return True
            