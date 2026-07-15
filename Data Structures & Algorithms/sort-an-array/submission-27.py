class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            temp = i
            for j in range(i + 1, n):
                if nums[j] <= nums[temp]:
                    temp = j
            nums[i], nums[temp] = nums[temp], nums[i]

        return nums