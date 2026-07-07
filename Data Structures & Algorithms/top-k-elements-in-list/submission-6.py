class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFreq = dict()

        for num in nums:
            numsFreq[num] = numsFreq.get(num, 0) + 1
        
        freqPair = list()
        for num, frq in numsFreq.items():
            freqPair.append([frq, num])

        freqPair.sort()
        res = list()
        for i in range(len(freqPair) - 1, -1, -1):
            if len(res) < k:
                res.append(freqPair[i][1])
            else:
                return res

        return res