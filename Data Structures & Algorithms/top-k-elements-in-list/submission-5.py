class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        eleFreq = dict()
        for num in nums:
            eleFreq[num] = eleFreq.get(num, 0) + 1
        
        heap = list()

        for num, frq in eleFreq.items():
            heapq.heappush(heap,[frq, num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = list()
        for num in heap:
            res.append(num[1])
        return res
     