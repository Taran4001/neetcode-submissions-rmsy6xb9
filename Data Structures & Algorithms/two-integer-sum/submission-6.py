class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, val in enumerate(nums):
            if target - val in seen:
                return [seen[target - val], index]
            seen[val] = index