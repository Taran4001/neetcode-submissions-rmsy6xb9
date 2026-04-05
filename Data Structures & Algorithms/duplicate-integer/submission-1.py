class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
            if num_freq[num] > 1:
                return True
        return False
            