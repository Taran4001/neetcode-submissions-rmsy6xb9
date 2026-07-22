class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        ans = list()
        countSequence = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] - nums[i - 1] > 1:
                ans.append(countSequence)
                countSequence = 1 
            else:
                countSequence += 1
        ans.append(countSequence)
        return max(ans) 
                