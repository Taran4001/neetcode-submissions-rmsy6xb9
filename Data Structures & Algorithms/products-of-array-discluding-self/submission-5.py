class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = list()
        product = 1
        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeroCount += 1
            
        for i in range(len(nums)):
            if zeroCount > 1:
                res.append(0)
            elif 0 in nums and nums[i] != 0:
                res.append(0)
            elif nums[i] == 0:
                res.append(product)
            else:
                res.append(product // nums[i])

        
        return res
            