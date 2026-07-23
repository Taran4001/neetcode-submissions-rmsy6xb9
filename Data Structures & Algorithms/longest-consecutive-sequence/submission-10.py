class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        length = 1
        nums.sort()
        if not nums:
            return 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if nums[i] == nums[i - 1]:
                continue
            
            if diff > 1:
                longest = max(longest, length)
                length = 1
            else:
                length += 1
                longest = max(longest, length)
            
        return longest