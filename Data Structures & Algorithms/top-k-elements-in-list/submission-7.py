class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = dict()

        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1

        freqBucket = [[] for _ in range((len(nums) + 1))]

        for num, frq in numFreq.items():
            freqBucket[frq].append(num)
        res = list()
        for i in range(len(freqBucket) - 1, 0, -1):
            for num in freqBucket[i]:    
                if len(res) < k:
                    res.append(num)
                else: 
                    return res
        return res