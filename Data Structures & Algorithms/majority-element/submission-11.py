class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majEleCount = 0
        majEle = None
        for num in nums:
            if majEleCount == 0:
                majEle = num
                majEleCount += 1
            elif num != majEle:
                majEleCount -= 1
            else:
                majEleCount += 1
        return majEle