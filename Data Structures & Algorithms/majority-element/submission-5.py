class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countElement = 0
        majElement = None

        for num in nums:
            if countElement == 0:
                majElement = num
                countElement += 1
            elif majElement == num:
                countElement += 1
            else:
                countElement -= 1
        return majElement