class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        majElement = None
        for num in nums:
            if counter == 0:
                majElement = num
                counter += 1
            elif num == majElement:
                counter += 1
            else:
                counter -= 1
        return majElement