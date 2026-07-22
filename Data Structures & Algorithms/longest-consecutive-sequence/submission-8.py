class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        currentLength = 1
        longest = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            if diff == 0:
                continue

            if diff > 1:
                longest = max(longest, currentLength)
                currentLength = 1
            else:
                currentLength += 1

        longest = max(longest, currentLength)
        return longest
                