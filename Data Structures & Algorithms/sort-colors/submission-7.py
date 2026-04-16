class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = p = 0
        j = len(nums) - 1

        while p <= j:
            if nums[p] == 2:
                nums[j], nums[p] = nums[p], nums[j]
                j -= 1
            elif nums[p] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                i += 1
                p += 1
            else:
                p += 1
