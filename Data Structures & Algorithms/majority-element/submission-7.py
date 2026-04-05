class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majElement = 0
        count = 0
        for num in nums:
            if count == 0:
                majElement = num
                count += 1
            elif majElement == num:
                count += 1
            elif majElement != num:
                count -= 1
        return majElement