class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ch_freq_s, ch_freq_t = dict(), dict()

        for i in range(len(s)):
            ch_freq_s[s[i]] = ch_freq_s.get(s[i], 0) + 1
            ch_freq_t[t[i]] = ch_freq_t.get(t[i], 0) + 1
        
        if ch_freq_s != ch_freq_t:
            return False
        
        return True