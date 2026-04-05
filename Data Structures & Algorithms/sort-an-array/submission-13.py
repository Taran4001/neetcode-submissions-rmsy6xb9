class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        while numsLen:
            p = 0
            q = 1
            while q < numsLen:
                if nums[p] > nums[q]:
                    nums[p], nums[q] = nums[q], nums[p]
                p += 1
                q += 1
            numsLen -= 1
        return nums