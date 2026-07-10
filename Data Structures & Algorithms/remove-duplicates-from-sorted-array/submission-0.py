class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        i = 1
        while i < len(nums):
            isEqual = False
            while i < len(nums) and nums[j] == nums[i]:
                i += 1
                isEqual = True
            if i < len(nums):
                j += 1
                nums[j] = nums[i]
            else:
                i += 1
        return j + 1