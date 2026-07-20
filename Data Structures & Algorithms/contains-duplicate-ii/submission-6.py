class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numIndex = dict()
        res = 0
        for i in range(len(nums)):
            if nums[i] in numIndex and i - numIndex[nums[i]] <= k:
                return True
            numIndex[nums[i]] = i
        
        return  False