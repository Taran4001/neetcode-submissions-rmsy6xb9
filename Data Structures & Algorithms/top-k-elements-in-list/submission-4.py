class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        eleFreq = dict()

        for num in nums:
            eleFreq[num] = eleFreq.get(num, 0) + 1
            
        eleFreqCount = [[] for _ in range(len(nums) + 1)]
        for num, frq in eleFreq.items():
            eleFreqCount[frq].append(num)
        
        res = list()
        for num in range(len(eleFreqCount) - 1, 0, -1):
            for ele in eleFreqCount[num]:
                if len(res) < k:
                    res.append(ele)
                else:
                    return res
        
        return res
