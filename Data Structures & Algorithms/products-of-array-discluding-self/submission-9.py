class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = list()
        suffixProduct = [0] * len(nums)
        res = list()
        prefix = suffix = 1
        for num in nums:
            prefix *= num
            prefixProduct.append(prefix)
            
        for i in range(len(nums) - 1, -1, -1):
            suffix *= nums[i]
            suffixProduct[i] = suffix
        
        for i in range(len(nums)):
            if i == 0:
                res.append(suffixProduct[i + 1])
            elif i == len(nums) - 1:
                res.append(prefixProduct[i - 1])
            else:
                res.append(prefixProduct[i - 1] * suffixProduct[i + 1])
        
        return res