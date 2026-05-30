class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        is_seen = dict()
        for i in range(len(nums)):
            if target - nums[i] in is_seen:
                return [is_seen[target - nums[i]], i]
            is_seen[nums[i]] = i