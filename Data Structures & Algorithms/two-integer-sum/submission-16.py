class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        isSeen = dict()
        for i in range(len(nums)):
            if target - nums[i] in isSeen:
                return [isSeen[target - nums[i]], i]
            isSeen[nums[i]] = i