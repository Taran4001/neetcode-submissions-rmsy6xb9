class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = p = 0
        j = len(nums) - 1
         
        while p <= j:
            if nums[p] == 0 and nums[i] == 0:
                p += 1
                i += 1
            elif nums[p] == 0:
                nums[p], nums[i] = nums[i], nums[p]
                i += 1
            elif nums[p] == 2:
                nums[p], nums[j] = nums[j], nums[p]
                j -= 1
            else:
                p += 1
        