class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i - 1
            while j > -1:
                if temp < nums[j]:
                    nums[j + 1] = nums[j]
                    j -= 1
                else:
                    break
            nums[j + 1] = temp
        return nums

