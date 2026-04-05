class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch_freq_s = dict()
        ch_freq_t = dict()

        for ch in s:
            ch_freq_s[ch] = ch_freq_s.get(ch, 0) + 1
        
        for ch in t:
            ch_freq_t[ch] = ch_freq_t.get(ch, 0) + 1
        
        if len(ch_freq_s) != len(ch_freq_t):
            return False
        for ch in s:
            if ch not in ch_freq_t or ch_freq_s[ch] != ch_freq_t[ch]:
                return False
        
        return True