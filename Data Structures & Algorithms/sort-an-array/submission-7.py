class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            minNum = nums[i]
            temp = i
            for j in range(i + 1, len(nums)):
                if minNum > nums[j]:
                    minNum = nums[j]
                    temp = j
            nums[i], nums[temp] = nums[temp], nums[i]
        return nums