class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        eleFreq = dict()

        for num in nums:
            eleFreq[num] = eleFreq.get(num, 0) + 1
        
        result = list()

        for _ in range(k):
            eleMaxFreq = 0
            countFreq = 0
            for key in eleFreq:
                if eleFreq[key] > countFreq:
                    countFreq = eleFreq[key]
                    eleMaxFreq = key


            result.append(eleMaxFreq)
            eleFreq.pop(eleMaxFreq)
        
        return result