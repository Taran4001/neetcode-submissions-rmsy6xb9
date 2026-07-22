class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        prefixProduct = [0] * numsLen
        sufixProduct = [0] * numsLen
        res = [0] * numsLen

        prefixProduct[0] = 1
        sufixProduct[-1] = 1

        preProduct = suProduct = 1
        for i in range(1, numsLen):
            preProduct *= nums[i - 1]
            prefixProduct[i] = preProduct

        for i in range(numsLen - 2, -1, -1):
            suProduct *= nums[i + 1]
            sufixProduct[i] = suProduct

        for i in range(numsLen):
            res[i] = (prefixProduct[i] * sufixProduct[i])
        
        return res