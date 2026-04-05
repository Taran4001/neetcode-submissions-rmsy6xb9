class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        is_seen = dict()

        for index, num in enumerate(nums):
            if target - num in is_seen:
                return [is_seen[target - num], index]
            is_seen[num] = index