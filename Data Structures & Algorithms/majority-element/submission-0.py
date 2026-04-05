class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqCount = dict()
        for num in nums:
            freqCount[num] = freqCount.get(num, 0) + 1
        majNum = None
        majCount = -1
        for num, count in freqCount.items():
            if count > majCount:
                majNum = num
                majCount = count
        return majNum
